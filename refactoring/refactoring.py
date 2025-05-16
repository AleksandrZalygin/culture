from typing import List, Dict, Union, Set, Any


def calculate_sum(numbers: List[float]) -> float:
    """Возвращает сумму элементов списка."""
    return sum(numbers)


def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


class Point:
    """Класс, представляющий точку в 2D-пространстве."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def calculate_area(self) -> float:
        """Вычисляет площадь (в данном случае — произведение координат)."""
        return self.x * self.y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Возвращает список только с четными числами."""
    return [num for num in numbers if num % 2 == 0]


def count_uppercase_letters(text: str) -> int:
    """Считает количество заглавных букв в строке."""
    return sum(1 for char in text if char.isupper())


def find_max_value(numbers: List[float]) -> float:
    """Находит максимальное значение в списке."""
    if not numbers:
        raise ValueError("Список не должен быть пустым")
    return max(numbers)


def compute_gcd(a: int, b: int) -> int:
    """Вычисляет НОД двух чисел по алгоритму Евклида."""
    while b:
        a, b = b, a % b
    return a


def reverse_string(text: str) -> str:
    """Возвращает строку в обратном порядке."""
    return text[::-1]


def factorial_recursive(n: int) -> int:
    """Вычисляет факториал числа рекурсивно."""
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    return 1 if n == 0 else n * factorial_recursive(n - 1)


def remove_duplicates(items: List[Any]) -> List[Any]:
    """Удаляет дубликаты из списка, сохраняя порядок."""
    seen = set()
    return [item for item in items if not (item in seen or seen.add(item))]


def count_char_frequency(text: str) -> Dict[str, int]:
    """Считает частоту каждого символа в строке."""
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Находит пересечение двух списков."""
    return list(set(list1) & set(list2))


def celsius_to_fahrenheit(celsius: float) -> float:
    """Конвертирует градусы Цельсия в Фаренгейты."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Конвертирует градусы Фаренгейта в Цельсии."""
    return (fahrenheit - 32) * 5 / 9


def count_vowels(text: str) -> int:
    """Считает количество гласных букв в строке."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)


def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]


def is_number_palindrome(number: int) -> bool:
    """Проверяет, является ли число палиндромом."""
    return str(number) == str(number)[::-1]


def filter_positive_numbers(numbers: List[float]) -> List[float]:
    """Фильтрует положительные числа из списка."""
    return [num for num in numbers if num > 0]


def count_digits(text: str) -> int:
    """Считает количество цифр в строке."""
    return sum(1 for char in text if char.isdigit())


def generate_zero_matrix(size: int) -> List[List[int]]:
    """Генерирует квадратную матрицу нулей заданного размера."""
    return [[0 for _ in range(size)] for _ in range(size)]


def get_odd_numbers(limit: int) -> List[int]:
    """Возвращает список нечетных чисел до заданного предела."""
    return [num for num in range(limit) if num % 2 != 0]


def clean_string(text: str) -> str:
    """Удаляет из строки все символы, кроме букв и цифр."""
    return ''.join(char for char in text if char.isalnum())


def main() -> None:
    """Демонстрация работы всех функций."""
    numbers = [1, 2, 3, 4, 5]
    print(f"Сумма чисел: {calculate_sum(numbers)}")
    print(f"Четные числа: {filter_even_numbers(numbers)}")
    print(f"Максимальное значение: {find_max_value(numbers)}")
    print(f"НОД 48 и 18: {compute_gcd(48, 18)}")
    print(f"Факториал 5: {factorial_recursive(5)}")
    print(f"Уникальные элементы: {remove_duplicates([1, 2, 2, 3])}")

    text = "Hello, World!"
    print(f"Количество заглавных букв: {count_uppercase_letters(text)}")
    print(f"Частота символов: {count_char_frequency(text)}")
    print(f"Реверс строки: {reverse_string(text)}")
    print(f"Гласные буквы: {count_vowels(text)}")
    print(f"Является ли 'racecar' палиндромом? {is_palindrome('racecar')}")

    point = Point(3, 4)
    print(f"Точка: {point}")
    print(f"Площадь (x*y): {point.calculate_area()}")

    print(f"25°C в Фаренгейтах: {celsius_to_fahrenheit(25)}")
    print(f"77°F в Цельсиях: {fahrenheit_to_celsius(77)}")


if __name__ == "__main__":
    main()
