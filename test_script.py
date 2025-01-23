def count_characters(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():  # Only include alphabetic characters
            counts[char] = counts.get(char, 0) + 1  # Increment count or set to 1
    print("DEBUG - Character Counts:", counts)  # Debug filtered character counts
    return counts

def count_words(text):
    words = text.split()  # Splits the text into a list of words
    return len(words)  # Counts the number of words

def generate_report(file_path):
    # Step 1: Read the file content
    with open(file_path, 'r') as file:
        text = file.read()  # Load the text file content
    
    # Debug: print raw file content
    print("DEBUG - Raw File Content:", text)

    # Step 2: Count the words and characters
    word_count = count_words(text)  # Count words in the document
    character_counts = count_characters(text)  # Get filtered alphabetic characters

    # Debug: print word count and character counts
    print("DEBUG - Word Count:", word_count)
    print("DEBUG - Character Counts:", character_counts)

    # Step 3: Sort the character counts by frequency descending, then alphabetically ascending
    sorted_characters = sorted

def generate_report(file_path):
        sorted_characters = sorted(character_counts.items(), key=lambda item: (-item[1], item[0]))
    print("DEBUG - Word Count:", word_count)
    print("DEBUG - Sorted Characters:", sorted_characters)  # Add this debug line
    with open(file_path, 'r') as file:
        text = file.read()  # Load the text file content

    word_count = count_words(text)  # Count words in the document
    character_counts = count_characters(text)  # Get filtered alphabetic characters

    # Start formatting the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Sort character counts by frequency descending, then alphabetically ascending
    sorted_characters = sorted(character_counts.items(), key=lambda item: (-item[1], item[0]))

    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print(f"--- End report ---")
