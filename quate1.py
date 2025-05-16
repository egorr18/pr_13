def simple_text_editor():
    print("Простий текстовий редактор")
    
    # Запит на створення нового файлу
    filename = input("Введіть ім'я нового текстового файлу (наприклад, 'mynotes.txt'): ")

    print("Введіть текст (рядок за рядком). Щоб завершити — введіть порожній рядок і натисніть Enter.")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Запис у файл
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"\nФайл '{filename}' збережено.")

    # Виведення вмісту
    print("\n=== Вміст файлу ===")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

# Запуск
simple_text_editor()
