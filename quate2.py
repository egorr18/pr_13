def analyze_file():
    print("=== Аналіз вмісту файлу ===")

    filename = input("Введіть ім'я файлу для аналізу (наприклад, 'mynotes.txt'): ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)

        print("\n=== Результати аналізу ===")
        print(f"Кількість рядків  : {num_lines}")
        print(f"Кількість слів    : {num_words}")
        print(f"Кількість символів: {num_chars}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте назву та повторіть спробу.")

# Запуск
analyze_file()
