def find_and_replace():
    print("=== Пошук і заміна у файлі ===")

    # Введення імені існуючого файлу
    original_file = input("Введіть ім'я файлу для обробки (наприклад, 'text.txt'): ")

    # Слова для пошуку і заміни
    search_word = input("Введіть слово або фразу для пошуку: ")
    replace_word = input("Введіть слово або фразу для заміни: ")

    # Зчитування вмісту файлу
    try:
        with open(original_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    # Заміна тексту
    modified_content = content.replace(search_word, replace_word)

    # Запис у новий файл
    new_filename = "modified_" + original_file
    with open(new_filename, "w", encoding="utf-8") as new_file:
        new_file.write(modified_content)

    print(f"\nЗаміна завершена. Новий файл збережено як '{new_filename}'.")

# Запуск
find_and_replace()
