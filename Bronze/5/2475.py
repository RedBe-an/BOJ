def get_verify_num(a, b, c, d, e):
    a = a * a
    b = b * b
    c = c * c
    d = d * d
    e = e * e
    return (a + b + c + d + e) % 10


a, b, c, d, e = map(int, input().split())
print(get_verify_num(a, b, c, d, e))
