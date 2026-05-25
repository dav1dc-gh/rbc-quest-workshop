"""Comprehensive tests for InventoryManager - the conversion target must pass these too."""

import pytest
from decimal import Decimal
from src.inventory_manager import InventoryManager, Product


class TestAddProduct:
    """Tests for adding products."""

    def test_add_valid_product(self):
        mgr = InventoryManager()
        product = mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        assert product.sku == "SKU001"
        assert product.name == "Widget"
        assert product.price == Decimal("9.99")
        assert product.quantity == 100
        assert product.category == "Hardware"

    def test_add_duplicate_sku_raises(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        with pytest.raises(ValueError, match="already exists"):
            mgr.add_product("SKU001", "Gadget", 19.99, 50, "Electronics")

    def test_add_negative_price_raises(self):
        mgr = InventoryManager()
        with pytest.raises(ValueError, match="Price cannot be negative"):
            mgr.add_product("SKU001", "Widget", -5.00, 100, "Hardware")

    def test_add_negative_quantity_raises(self):
        mgr = InventoryManager()
        with pytest.raises(ValueError, match="Quantity cannot be negative"):
            mgr.add_product("SKU001", "Widget", 9.99, -1, "Hardware")

    def test_add_empty_sku_raises(self):
        mgr = InventoryManager()
        with pytest.raises(ValueError, match="SKU and name cannot be empty"):
            mgr.add_product("", "Widget", 9.99, 100, "Hardware")

    def test_add_empty_name_raises(self):
        mgr = InventoryManager()
        with pytest.raises(ValueError, match="SKU and name cannot be empty"):
            mgr.add_product("SKU001", "", 9.99, 100, "Hardware")

    def test_add_zero_price(self):
        mgr = InventoryManager()
        product = mgr.add_product("FREE01", "Freebie", 0.0, 50, "Promo")
        assert product.price == Decimal("0")

    def test_add_with_custom_min_stock(self):
        mgr = InventoryManager()
        product = mgr.add_product("SKU001", "Widget", 9.99, 5, "Hardware", min_stock_level=3)
        assert not product.is_low_stock()


class TestRemoveProduct:
    """Tests for removing products."""

    def test_remove_existing_product(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        removed = mgr.remove_product("SKU001")
        assert removed.sku == "SKU001"

    def test_remove_nonexistent_raises(self):
        mgr = InventoryManager()
        with pytest.raises(KeyError):
            mgr.remove_product("NOEXIST")

    def test_remove_then_add_same_sku(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        mgr.remove_product("SKU001")
        product = mgr.add_product("SKU001", "New Widget", 14.99, 50, "Hardware")
        assert product.name == "New Widget"


class TestUpdateStock:
    """Tests for stock updates."""

    def test_increase_stock(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        new_qty = mgr.update_stock("SKU001", 50)
        assert new_qty == 150

    def test_decrease_stock(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        new_qty = mgr.update_stock("SKU001", -30)
        assert new_qty == 70

    def test_decrease_to_zero(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        new_qty = mgr.update_stock("SKU001", -100)
        assert new_qty == 0

    def test_decrease_below_zero_raises(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 10, "Hardware")
        with pytest.raises(ValueError, match="Cannot reduce stock below 0"):
            mgr.update_stock("SKU001", -11)

    def test_update_nonexistent_raises(self):
        mgr = InventoryManager()
        with pytest.raises(KeyError):
            mgr.update_stock("NOEXIST", 10)


class TestPricing:
    """Tests for price calculation with discounts."""

    def test_price_no_discount(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        assert mgr.calculate_price("SKU001", 3) == Decimal("29.97")

    def test_price_with_discount(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 10.00, 100, "Hardware")
        mgr.set_category_discount("Hardware", 15.0)
        # 10 * 3 = 30, 15% off = 25.50
        assert mgr.calculate_price("SKU001", 3) == Decimal("25.50")

    def test_price_rounding(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        mgr.set_category_discount("Hardware", 33.33)
        # 9.99 * 2 = 19.98, 33.33% off = 19.98 * 0.6667 = 13.3193...
        result = mgr.calculate_price("SKU001", 2)
        assert result == Decimal("13.32")

    def test_price_quantity_one(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 25.50, 100, "Hardware")
        assert mgr.calculate_price("SKU001") == Decimal("25.50")

    def test_price_nonexistent_raises(self):
        mgr = InventoryManager()
        with pytest.raises(KeyError):
            mgr.calculate_price("NOEXIST", 1)

    def test_price_zero_quantity_raises(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        with pytest.raises(ValueError, match="Quantity must be at least 1"):
            mgr.calculate_price("SKU001", 0)

    def test_discount_out_of_range_raises(self):
        mgr = InventoryManager()
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            mgr.set_category_discount("Hardware", 101.0)

    def test_discount_negative_raises(self):
        mgr = InventoryManager()
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            mgr.set_category_discount("Hardware", -5.0)

    def test_100_percent_discount(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 100, "Hardware")
        mgr.set_category_discount("Hardware", 100.0)
        assert mgr.calculate_price("SKU001", 5) == Decimal("0.00")


class TestReporting:
    """Tests for inventory reporting."""

    def test_low_stock_detection(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 5, "Hardware")  # below default 10
        mgr.add_product("SKU002", "Gadget", 19.99, 50, "Electronics")  # above
        low = mgr.get_low_stock_products()
        assert len(low) == 1
        assert low[0].sku == "SKU001"

    def test_low_stock_sorted_by_quantity(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 9.99, 5, "Hardware")
        mgr.add_product("SKU002", "Gadget", 19.99, 2, "Electronics")
        mgr.add_product("SKU003", "Doohickey", 4.99, 8, "Hardware")
        low = mgr.get_low_stock_products()
        assert [p.quantity for p in low] == [2, 5, 8]

    def test_inventory_value(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 10.00, 5, "Hardware")
        mgr.add_product("SKU002", "Gadget", 20.00, 3, "Electronics")
        assert mgr.get_inventory_value() == Decimal("110.00")

    def test_inventory_value_empty(self):
        mgr = InventoryManager()
        assert mgr.get_inventory_value() == Decimal("0.00")

    def test_products_by_category(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Zebra Widget", 9.99, 100, "Hardware")
        mgr.add_product("SKU002", "Alpha Gadget", 19.99, 50, "Hardware")
        mgr.add_product("SKU003", "Phone", 999.99, 10, "Electronics")
        hardware = mgr.get_products_by_category("Hardware")
        assert len(hardware) == 2
        assert hardware[0].name == "Alpha Gadget"  # sorted by name
        assert hardware[1].name == "Zebra Widget"

    def test_search_products(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Blue Widget", 9.99, 100, "Hardware")
        mgr.add_product("SKU002", "Red Widget", 19.99, 50, "Hardware")
        mgr.add_product("SKU003", "Phone Case", 4.99, 200, "Accessories")
        results = mgr.search_products("widget")
        assert len(results) == 2

    def test_search_case_insensitive(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Blue Widget", 9.99, 100, "Hardware")
        results = mgr.search_products("BLUE")
        assert len(results) == 1

    def test_generate_report(self):
        mgr = InventoryManager()
        mgr.add_product("SKU001", "Widget", 10.00, 5, "Hardware")
        mgr.add_product("SKU002", "Gadget", 20.00, 50, "Electronics")
        report = mgr.generate_report()
        assert report["total_products"] == 2
        assert report["total_value"] == "1050.00"
        assert report["low_stock_count"] == 1
        assert report["categories"] == {"Hardware": 1, "Electronics": 1}
