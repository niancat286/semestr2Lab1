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


def count_word(words):
    word_count = {}
    for word in words:
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count






print(clean_file('inputfile.txt'))
print(count_word(clean_file('inputfile.txt')))
