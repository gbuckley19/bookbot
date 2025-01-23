def count_characters(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():  # Only include alphabetic characters
            counts[char] = counts.get(char, 0) + 1  # Increment count or set to 1
    return counts


def count_words(text):
    words = text.split()  # Splits the text into a list of words
    return len(words)  # Counts the number of words


def generate_report(file_path):
    # Step 1: Read the file content
    with open(file_path, 'r') as file:
        text = file.read()  # Load the text file content

    # Step 2: Count the words and characters
    word_count = count_words(text)
    character_counts = count_characters(text)

    # Step 3: Sort the character counts
    sorted_characters = sorted(character_counts.items(), key=lambda item: (-item[1], item[0]))

    # Step 4: Begin formatting the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Step 5: Print out the sorted character counts in order
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


# Step 6: Main entry point for the script
if __name__ == "__main__":
    # Replace this with the path to your text file
    generate_report("books/frankenstein.txt")