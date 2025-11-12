
"""
Задание 2: MVP dating-сервиса
"""

def create_pairs(boys, girls):
    """
    Создает идеальные пары после сортировки списков
    """
    if len(boys) != len(girls):
        return "Внимание, кто-то может остаться без пары!"
    
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    
    pairs = []
    for i in range(len(boys_sorted)):
        pairs.append(f"{boys_sorted[i]} и {girls_sorted[i]}")
    
    return pairs


def main_task2():
    """Основная функция для задания 2"""
    print("=== ЗАДАНИЕ 2 ===")
    print("MVP dating-сервиса")
    print("-" * 30)
    
    print("Пример 1:")
    boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    
    result1 = create_pairs(boys1, girls1)
    if isinstance(result1, list):
        print("Идеальные пары:")
        for pair in result1:
            print(pair)
    else:
        print(result1)
    
    print("\nПример 2:")
    boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
    girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    
    result2 = create_pairs(boys2, girls2)
    if isinstance(result2, list):
        print("Идеальные пары:")
        for pair in result2:
            print(pair)
    else:
        print(result2)
    
    print("\n" + "=" * 40)
    print("Интерактивный режим:")
    print("=" * 40)
    
    while True:
        print("\nВведите списки имен:")
        boys_input = input("Юноши (через запятую): ")
        girls_input = input("Девушки (через запятую): ")
        
        if boys_input.lower() == 'exit' or girls_input.lower() == 'exit':
            print("Задание 2 завершено.")
            break
        
        boys_list = [name.strip() for name in boys_input.split(',') if name.strip()]
        girls_list = [name.strip() for name in girls_input.split(',') if name.strip()]
        
        result = create_pairs(boys_list, girls_list)
        if isinstance(result, list):
            print("Идеальные пары:")
            for pair in result:
                print(pair)
        else:
            print(result)


if __name__ == "__main__":
    main_task2()
