import re
from collections.abc import Callable, Iterator
from decimal import Decimal


def generator_numbers(text: str) -> Iterator[Decimal]:
    """
    Генератор, витягує з тексту всі числа формату 0.00
    та повертає їх як об'єкти Decimal якщо вони відокремлені
    пробілами з обох боків або число на початку строки або за ним кінець строки
    """
    pattern = r"(?:(?<=\s)|^)\d+\.\d{2}(?=\s|$)"
    for income in re.finditer(pattern, text):
        yield Decimal(income.group())


def sum_profit(text: str, numbers: Callable[[str], Iterator[Decimal]]):
    """
    Підраховує загальний дохід, використовуючи функцію генератор,
    яка генерує всі грошові значення з тексту.
    """
    income = numbers(text)
    return sum(income)


def main() -> None:
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
