def check_parity(a: int, b: int, c: int) -> bool:
    del_a = a % 2
    del_b = b % 2
    del_c = c % 2
    return del_a == del_b == del_c


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
