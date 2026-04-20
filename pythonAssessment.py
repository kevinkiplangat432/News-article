import re
from collections import Counter
# paramenters: filename (string), target_word (strin
def read_file(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# print('Hello, World!')
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
    if result:
        return result[0][0]
    else:
        return ""



def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    total = 0
    for word in words:
        total += len(word)

    return total / len(words)

def count_paragraphs(text):
    if text == "":
        return 1
    paragraphs = text.strip().split("\n\n")
    """
    Count the number of non-empty paragraphs in the text.
    A paragraph is defined as a block of text separated by two newline characters ("\n\n").

    The function first checks if the input text is empty. If it is, it returns 1, as an empty text is considered to have one paragraph.
    If the text is not empty, it splits the text into paragraphs using the split method with "\n\n" as the delimiter
    """
    count = 0
    for p in paragraphs:
        if p.strip():
            count += 1
    return count

def count_sentences(text):
    if text == "":
        return 1
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count
 

def main():
    file = "newsArticle.txt"
    text = read_file(file)

    i = 0
    while i < 1:
        if text:
            word_to_count = input("Enter a word to count: ")
            print(count_specific_word(text, word_to_count))
            
            print(identify_most_common_word(text))
            print(calculate_average_word_length(text))
            print(count_paragraphs(text))
            print(count_sentences(text))
        i += 1
        main()

    


if __name__ == "__main__":
    main()