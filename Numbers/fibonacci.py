def fib(n: int) -> int:
    """Return the Nth Fibonacci Number"""
    return fib(n - 1) + fib(n - 2) if n > 2 else 1

def main() -> None:
    n = int(input("Which fibonacci number do you want to see? "))
    print(f"{fib(n)} is the {n}th fibonacci number.")

main()