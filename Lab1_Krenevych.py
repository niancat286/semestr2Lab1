def clean_file(fileID):
    try:
        with open(fileID, 'r', encoding='utf-8') as f:
            text = f.read()
        words = text.lower().replace('\n', ' ').split()
        clean_words = [word.strip(".,!?") for word in words]
        return clean_words
    except FileNotFoundError:
        print(f"Помилка: Файл {fileID} не знайдено.")
        return []


print(clean_file('inputfile.txt'))
