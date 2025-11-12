
"""
Задание 1: Поиск средних букв в слове
"""

def find_middle_letters(word):
    """
    Находит среднюю букву/буквы в слове
    """
    length = len(word)
    
    if length == 0:
        return "Слово пустое"
    
    middle_index = length // 2
    
    if length % 2 == 1:
        return word[middle_index]
    else:
        return word[middle_index - 1:middle_index + 1]


def main_task1():
    """Основная функция для задания 1"""
    print("=== ЗАДАНИЕ 1 ===")
    print("Поиск средних букв в слове")
    print("-" * 30)
    
    test_cases = ['test', 'testing']
    
    print("Тестовые примеры из условия:")
    for word in test_cases:
        result = find_middle_letters(word)
        print(f"word = '{word}' \t Результат: {result}")
    
    print("\n" + "=" * 40)
    print("Интерактивный режим:")
    print("=" * 40)
    
    while True:
        user_input = input("\nВведите слово (или 'exit' для выхода): ")
        
        if user_input.lower() == 'exit':
            print("Задание 1 завершено.")
            break
        
        result = find_middle_letters(user_input)
        print(f"word = '{user_input}' \t Результат: {result}")


if __name__ == "__main__":
    main_task1()
