"""
InventoryManager - A product inventory system with pricing and stock management.

Supports adding/removing products, stock tracking, price calculations with
discounts, and inventory reporting.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


@dataclass
class Product:
    """Represents a product in the inventory."""
    sku: str
    name: str
    price: Decimal
    quantity: int
    category: str
    min_stock_level: int = 10

    def is_low_stock(self) -> bool:
        """Check if product is below minimum stock level."""
        return self.quantity < self.min_stock_level


class InventoryManager:
    """Manages a product inventory with pricing and stock operations."""

    def __init__(self):
        self._products: Dict[str, Product] = {}
        self._discount_rules: Dict[str, Decimal] = {}  # category -> discount percentage

    def add_product(self, sku: str, name: str, price: float, quantity: int,
                    category: str, min_stock_level: int = 10) -> Product:
        """
        Add a new product to the inventory.

        Args:
            sku: Unique product identifier
            name: Product display name
            price: Unit price (will be stored as Decimal)
            quantity: Initial stock quantity
            category: Product category
            min_stock_level: Threshold for low-stock alerts

        Returns:
            The created Product

        Raises:
            ValueError: If SKU already exists or inputs are invalid
        """
        if sku in self._products:
            raise ValueError(f"Product with SKU '{sku}' already exists")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if not sku or not name:
            raise ValueError("SKU and name cannot be empty")

        product = Product(
            sku=sku,
            name=name,
            price=Decimal(str(price)),
            quantity=quantity,
            category=category,
            min_stock_level=min_stock_level,
        )
        self._products[sku] = product
        return product

    def remove_product(self, sku: str) -> Product:
        """
        Remove a product from the inventory.

        Args:
            sku: The product SKU to remove

        Returns:
            The removed Product

        Raises:
            KeyError: If SKU does not exist
        """
        if sku not in self._products:
            raise KeyError(f"Product with SKU '{sku}' not found")
        return self._products.pop(sku)

    def update_stock(self, sku: str, quantity_change: int) -> int:
        """
        Update stock quantity for a product (positive to add, negative to remove).

        Args:
            sku: Product SKU
            quantity_change: Amount to add (positive) or remove (negative)

        Returns:
            New stock quantity

        Raises:
            KeyError: If SKU does not exist
            ValueError: If resulting quantity would be negative
        """
        if sku not in self._products:
            raise KeyError(f"Product with SKU '{sku}' not found")

        product = self._products[sku]
        new_quantity = product.quantity + quantity_change

        if new_quantity < 0:
            raise ValueError(
                f"Cannot reduce stock below 0. Current: {product.quantity}, "
                f"Requested change: {quantity_change}"
            )

        product.quantity = new_quantity
        return new_quantity

    def set_category_discount(self, category: str, discount_percent: float) -> None:
        """
        Set a discount percentage for an entire category.

        Args:
            category: The category name
            discount_percent: Discount as percentage (e.g., 15.0 for 15%)

        Raises:
            ValueError: If discount is not between 0 and 100
        """
        if not (0 <= discount_percent <= 100):
            raise ValueError("Discount must be between 0 and 100")
        self._discount_rules[category] = Decimal(str(discount_percent))

    def calculate_price(self, sku: str, quantity: int = 1) -> Decimal:
        """
        Calculate the total price for a given quantity, applying any category discounts.

        Uses banker's rounding (ROUND_HALF_UP) for currency precision.

        Args:
            sku: Product SKU
            quantity: Number of units

        Returns:
            Total price after discount, rounded to 2 decimal places

        Raises:
            KeyError: If SKU does not exist
            ValueError: If quantity is less than 1
        """
        if sku not in self._products:
            raise KeyError(f"Product with SKU '{sku}' not found")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")

        product = self._products[sku]
        subtotal = product.price * quantity

        # Apply category discount if one exists
        if product.category in self._discount_rules:
            discount = self._discount_rules[product.category]
            discount_amount = subtotal * (discount / Decimal("100"))
            subtotal = subtotal - discount_amount

        return subtotal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def get_low_stock_products(self) -> List[Product]:
        """
        Get all products that are below their minimum stock level.

        Returns:
            List of Products with low stock, sorted by quantity (ascending)
        """
        low_stock = [p for p in self._products.values() if p.is_low_stock()]
        return sorted(low_stock, key=lambda p: p.quantity)

    def get_inventory_value(self) -> Decimal:
        """
        Calculate total value of all inventory (sum of price * quantity).

        Returns:
            Total inventory value rounded to 2 decimal places
        """
        total = Decimal("0")
        for product in self._products.values():
            total += product.price * product.quantity
        return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def get_products_by_category(self, category: str) -> List[Product]:
        """
        Get all products in a specific category.

        Args:
            category: Category name to filter by

        Returns:
            List of products in the category, sorted by name
        """
        products = [p for p in self._products.values() if p.category == category]
        return sorted(products, key=lambda p: p.name)

    def search_products(self, query: str) -> List[Product]:
        """
        Search products by name (case-insensitive substring match).

        Args:
            query: Search string

        Returns:
            List of matching products, sorted by name
        """
        query_lower = query.lower()
        matches = [
            p for p in self._products.values()
            if query_lower in p.name.lower()
        ]
        return sorted(matches, key=lambda p: p.name)

    def generate_report(self) -> Dict[str, any]:
        """
        Generate a summary report of the inventory.

        Returns:
            Dictionary with total_products, total_value, low_stock_count,
            and categories breakdown
        """
        categories: Dict[str, int] = {}
        for product in self._products.values():
            categories[product.category] = categories.get(product.category, 0) + 1

        return {
            "total_products": len(self._products),
            "total_value": str(self.get_inventory_value()),
            "low_stock_count": len(self.get_low_stock_products()),
            "categories": categories,
        }
