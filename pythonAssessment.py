import re
from collections import Counter

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

def count_specific_word(text, target_word):
    words = re.findall(r'\b\w+\b', text.lower())
    count = 0
    for word in words:
        if word == target_word.lower():
            count += 1
    return count

def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    result = counter.most_common(1)
    return result[0][0] if result else ""

def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

def count_paragraphs(text):
    paragraphs = text.strip().split("\n\n")
    count = 0
    for p in paragraphs:
        if p.strip():
            count += 1
    return count

def count_sentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count

def main():
    filename = "newsArticle.txt"
    text = read_file(filename)
    if not text:
        return
    cleaned_word = "the"
    print(count_specific_word(text, cleaned_word))
    print(identify_most_common_word(text))
    print(calculate_average_word_length(text))
    print(count_paragraphs(text))
    print(count_sentences(text))

if __name__ == "__main__":
    main()