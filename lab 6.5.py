def word_count(text):
    words = text.split()
    return len(words)

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def count_substring(text, substring):
    return text.count(substring)

def extract_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return unique_words

def main():
    print("Hello! Welcome to the Text Processing Program!")
    text = input("Please enter your text: ")
    print("1. Word count")
    print("2. Longest word")
    print("3. Count of substring")
    print("4. Unique words")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("Word count:", word_count(text))
        elif choice == '2':
            print("Longest word:", find_longest_word(text))
        elif choice == '3':
            substring = input("Enter the substring to count: ")
            print("Occurrences of substring:", count_substring(text, substring))
        elif choice == '4':
            print("Unique words:", extract_unique_words(text))
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
