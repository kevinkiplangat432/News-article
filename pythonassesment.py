import re
from collections import Counter


#Read file
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Make sure it's in the same directory.")
        return ""


#Clean text (for word-based analysis)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


#Count specific word
def count_specific_word(text, target_word):
    words = text.split()
    return words.count(target_word.lower())


#Most common word
def get_most_common_word(text):
    words = text.split()
    counter = Counter(words)
    most_common = counter.most_common(1)
    return most_common[0] if most_common else ("", 0)


#Average word length
def calculate_average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


#Count paragraphs
def count_paragraphs(text):
    paragraphs = text.strip().split("\n\n")
    return len([p for p in paragraphs if p.strip()])


#Count sentences
def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


#Main program
def main():
    filename = "newsArticle.txt" 

    text = read_file(filename)

    if not text:
        return

    cleaned_text = clean_text(text)

    target_word = input("Enter a word to search: ")

    print("\nTxt analysis results")

    # Word count
    word_count = count_specific_word(cleaned_text, target_word)
    print(f"Occurrences of '{target_word}': {word_count}")

    # Most common word
    word, count = get_most_common_word(cleaned_text)
    print(f"Most common word: '{word}' (used {count} times)")

    # Average word length
    avg_length = calculate_average_word_length(cleaned_text)
    print(f"Average word length: {avg_length:.2f}")

    # Paragraph count
    paragraphs = count_paragraphs(text)
    print(f"Number of paragraphs: {paragraphs}")

    # Sentence count
    sentences = count_sentences(text)
    print(f"Number of sentences: {sentences}")


# Run program
if __name__ == "__main__":
    main()