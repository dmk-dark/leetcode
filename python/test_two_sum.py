import pytest
from two_sum import two_sum

def test_two_sum():
    # Тест на корректный результат
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    # Тест на отсутствие результата
    assert two_sum([2, 4, 6], 11) == []
    # Тест с отрицательными числами
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    # Тест на множественные пары
    assert two_sum([1, 1, 2, 45], 46) == [1, 3]

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
