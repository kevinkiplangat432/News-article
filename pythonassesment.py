import re
from collections import Counter


def readFile(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Make sure it's in the same directory.")
        return ""


def textCleanup(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


#count specific word
def countSpecificWord(text, target_word):
    words = text.split()
    return words.count(target_word.lower())


#most common word
def getMostCommonWord(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(1)[0] if counter else ("", 0)


#average word length
def calculateAverageWordLength(text):
    words = text.split()

    if not words:
        return 0

    total_length = 0
    for word in words:
        total_length += len(word)

    return total_length / len(words)


#count paragraphs
def countParagraphs(text):
    paragraphs = text.strip().split("\n\n")
    count = 0

    for p in paragraphs:  
        if p.strip():     
            count += 1

    return count


# count sentences 
def countSentences(text):
    count = 0

    for char in text:  
        if char in ".!?":  
            count += 1

    return count


# While loop for input validation
def get_valid_word():
    while True:  
        word = input("Enter a word to search: ").strip()

        if word:  
            return word
        else:
            print("Please enter a valid word.")



def main():
    filename = "newsArticle.txt"

    text = readFile(filename)

    if not text:
        return

    cleaned_text = textCleanup(text)

    target_word = get_valid_word()

    print("\n text analysis ")

    word_count = countSpecificWord(cleaned_text, target_word)
    print(f"Occurrences of '{target_word}': {word_count}")
   
    if word_count > 0:
        print("The word exists in the article.")
    else:
        print("The word was not found in the article.")

    word, count = getMostCommonWord(cleaned_text)
    print(f"Most common word: '{word}' (used {count} times)")
    avg_length = calculateAverageWordLength(cleaned_text)
    print(f"Average word length: {avg_length:.2f}")

  
    paragraphs = countParagraphs(text)
    print(f"Number of paragraphs: {paragraphs}")

  
    sentences = countSentences(text)
    print(f"Number of sentences: {sentences}")



if __name__ == "__main__":
    main()