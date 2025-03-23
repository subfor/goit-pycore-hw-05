from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(number: int) -> int:
        # nonlocal cache
        if number in cache:
            return cache[number]
        if number <= 0:
            result = 0
        elif number in (1, 2):
            result = 1
        else:
            result = fibonacci(number - 1) + fibonacci(number - 2)
        cache[number] = result
        return result

    return fibonacci


if __name__ == "__main__":
    f = caching_fibonacci()
    print(f(1))
    print(f(2))
    print(f(10))
    print(f(15))
    print(f(-1))
