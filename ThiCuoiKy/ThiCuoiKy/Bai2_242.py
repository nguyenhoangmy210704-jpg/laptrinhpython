def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def bang_cuu_chuong(a, b):

    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a

    for i in range(start, end + 1):
        print(f"\nBảng cửu chương {i}")

        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")


def liet_ke_so_nguyen_to(n):
    print(f"\nCác số nguyên tố nhỏ hơn {n} là:")

    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=" ")

    print()


def uoc_so_nguyen_to(n):
    print(f"\nCác ước số nguyên tố của {n} là:")

    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            print(i, end=" ")

    print()


a, b = map(int, input("Nhập a,b (cách nhau dấu phẩy): ").split(","))

bang_cuu_chuong(a, b)

n = int(input("\nNhập n: "))
liet_ke_so_nguyen_to(n)


n2 = int(input("\nNhập n: "))
uoc_so_nguyen_to(n2)
