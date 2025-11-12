
"""
Главная программа - объединяет оба задания
"""

def main():
    """Главная функция программы"""
    print("ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ!")
    print("=" * 50)
    
    while True:
        print("\nВыберите задание:")
        print("1 - Поиск средних букв в слове")
        print("2 - MVP dating-сервиса")
        print("3 - Запустить все задания последовательно")
        print("0 - Выход")
        
        choice = input("\nВаш выбор (0-3): ")
        
        if choice == '1':
            import task1_middle_letters
            task1_middle_letters.main_task1()
        elif choice == '2':
            import task2_dating_service
            task2_dating_service.main_task2()
        elif choice == '3':
            print("\n" + "="*50)
            import task1_middle_letters
            task1_middle_letters.main_task1()
            print("\n" + "="*50)
            import task2_dating_service
            task2_dating_service.main_task2()
        elif choice == '0':
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
