import re
from collections import Counter

def readFile(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

def textCleanup(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def countSpecificWord(text, target_word):
    words = text.split()
    return words.count(target_word.lower())

def getMostCommonWord(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(1)[0] if counter else ("", 0)

def calculateAverageWordLength(text):
    words = text.split()
    if not words:
        return 0
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)

def countParagraphs(text):
    paragraphs = text.strip().split("\n\n")
    count = 0
    for p in paragraphs:
        if p.strip():
            count += 1
    return count

def countSentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count

def main():
    filename = "newsArticle.txt"
    text = readFile(filename)
    if not text:
        return
    cleaned_text = textCleanup(text)
    target_word = "the"
    word_count = countSpecificWord(cleaned_text, target_word)
    print(word_count)
    word, count = getMostCommonWord(cleaned_text)
    print(word)
    avg_length = calculateAverageWordLength(cleaned_text)
    print(avg_length)
    paragraphs = countParagraphs(text)
    print(paragraphs)
    sentences = countSentences(text)
    print(sentences)

if __name__ == "__main__":
    main()