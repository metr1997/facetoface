import argparse

def main():
  
    parser = argparse.ArgumentParser(description="Скрипт для вывода строки с учетом опций.")
    
    
    parser.add_argument("number", type=int, help="Число, связанное со строкой")
    parser.add_argument("string", type=str, help="Строка для вывода")
    
   
    parser.add_argument("--verbose", action="store_true", help="Выводить дополнительную информацию")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки")

    
    args = parser.parse_args()


    if args.verbose:
        print(f"Полученное число: {args.number}")
        print(f"Полученная строка: {args.string}")
        print(f"Количество повторений: {args.repeat}")

    
    for _ in range(args.repeat):
        print(args.string)

if __name__ == "__main__":
    main()

    # Запуск скрипта 'python zadanie4.py 3 "Привет, мир!" --verbose --repeat 2'