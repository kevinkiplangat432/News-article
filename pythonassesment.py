import re
from collections import Counter


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Make sure it's in the same directory.")
        return ""


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


#count specific word
def count_specific_word(text, target_word):
    words = text.split()
    return words.count(target_word.lower())


#most common word
def get_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(1)[0] if counter else ("", 0)


#average word length
def calculate_average_word_length(text):
    words = text.split()

    if not words:
        return 0

    total_length = 0
    for word in words:
        total_length += len(word)

    return total_length / len(words)


#count paragraphs
def count_paragraphs(text):
    paragraphs = text.strip().split("\n\n")
    count = 0

    for p in paragraphs:  
        if p.strip():     
            count += 1

    return count


# count sentences 
def count_sentences(text):
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


# Main function
def main():
    filename = "newsArticle.txt"

    text = read_file(filename)

    if not text:
        return

    cleaned_text = clean_text(text)

    target_word = get_valid_word()

    print("\n text analysis ")

    word_count = count_specific_word(cleaned_text, target_word)
    print(f"Occurrences of '{target_word}': {word_count}")
   
    if word_count > 0:
        print("The word exists in the article.")
    else:
        print("The word was not found in the article.")

    word, count = get_most_common_word(cleaned_text)
    print(f"Most common word: '{word}' (used {count} times)")
    avg_length = calculate_average_word_length(cleaned_text)
    print(f"Average word length: {avg_length:.2f}")

  
    paragraphs = count_paragraphs(text)
    print(f"Number of paragraphs: {paragraphs}")

  
    sentences = count_sentences(text)
    print(f"Number of sentences: {sentences}")



if __name__ == "__main__":
    main()