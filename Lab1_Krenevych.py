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


def sort_by_freq(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    fileID = input("Введіть імʼя файлу з текстом: ")

    words = clean_file(fileID)
    if words:
        word_count = count_word(words)
        sort_by_freq(word_count)

