la_boi_so = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập số nguyên n: "))

if la_boi_so(n):
    print(f"{n} là bội số của 13 hoặc 19")
else:
    print(f"{n} không là bội số của 13 hoặc 19")


tam_giac_hop_le = lambda a, b, c: (
    a + b > c and a + c > b and b + c > a
)

a = int(input("\nNhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if tam_giac_hop_le(a, b, c):

    if a == b == c:
        print("Đây là tam giác đều")

    elif a == b or a == c or b == c:
        print("Đây là tam giác cân")

    elif a**2 + b**2 == c**2 or \
         a**2 + c**2 == b**2 or \
         b**2 + c**2 == a**2:
        print("Đây là tam giác vuông")

    else:
        print("Đây là tam giác thường")

else:
    print("a, b, c không phải là 3 cạnh của tam giác")
