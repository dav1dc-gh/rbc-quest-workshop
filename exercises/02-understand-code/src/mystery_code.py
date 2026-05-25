"""
Mystery code - Three working but deliberately obfuscated functions.
Your task: understand what they do, then refactor them into clean code.
"""


def fn1(d, s=None, e=None):
    s = s if s is not None else 0
    e = e if e is not None else len(d) - 1
    if s >= e:
        return d
    p = d[e]
    i = s
    for j in range(s, e):
        if d[j] <= p:
            d[i], d[j] = d[j], d[i]
            i += 1
    d[i], d[e] = d[e], d[i]
    fn1(d, s, i - 1)
    fn1(d, i + 1, e)
    return d


def fn2(t, k):
    r = []
    n = len(t)
    def b(s, i, c):
        if c == 0:
            r.append(s[:])
            return
        if i >= n:
            return
        for j in range(i, n):
            if j > i and t[j] == t[j-1]:
                continue
            if t[j] > c:
                break
            s.append(t[j])
            b(s, j + 1, c - t[j])
            s.pop()
    t.sort()
    b([], 0, k)
    return r


def fn3(s):
    n = len(s)
    if n < 2:
        return s
    dp = [0] * n
    dp[0] = 1
    mx = 0
    mi = 0
    for i in range(1, n):
        l = 0
        r = mx - i if mx > i else 0
        if i < mx:
            m = 2 * mi - i
            if m >= 0:
                l = min(dp[m], mx - i)
        while i - l - 1 >= 0 and i + l + 1 < n and s[i - l - 1] == s[i + l + 1]:
            l += 1
        dp[i] = l
        if i + l > mx:
            mx = i + l
            mi = i
    ci = 0
    cl = 0
    for i in range(n):
        if dp[i] > cl:
            cl = dp[i]
            ci = i
    return s[ci - cl:ci + cl + 1]
