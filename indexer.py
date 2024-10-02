import json
from collections import defaultdict

# Step 1: Define a function to build an inverted index from text
def build_inverted_index(text):
    inverted_index = defaultdict(list)
    words = text.split()  # Basic tokenization
    for pos, word in enumerate(words):
        cleaned_word = ''.join(filter(str.isalnum, word)).lower()  # Remove punctuation and convert to lowercase
        if cleaned_word:
            inverted_index[cleaned_word].append(pos)
    return inverted_index

# Step 2: Define a function to save the index as a JSON file
def save_inverted_index_to_json(inverted_index, filename):
    with open(filename, 'w') as f:
        json.dump(inverted_index, f)
    print(f"Inverted index saved to {filename}")

# Step 3: Define a function to load the index from a JSON file
def load_inverted_index_from_json(filename):
    with open(filename, 'r') as f:
        inverted_index = json.load(f)
    print(f"Inverted index loaded from {filename}")
    return inverted_index

# Step 4: Define a function to search for a word in the index
def search_word_in_index(word, inverted_index):
    word = word.lower()
    if word in inverted_index:
        return inverted_index[word]
    else:
        return None

# Step 5: Define a function to read the text from a .txt file
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# Example usage:
if __name__ == "__main__":
    # Step 6: Read the book text from a .txt file
    text_file = 'awakening.txt'  # Replace with the actual path to your .txt file
    book_text = read_text_from_file(text_file)
    
    # Step 7: Build the inverted index from the text
    inverted_index = build_inverted_index(book_text)

    # Step 8: Save the inverted index to a JSON file
    save_inverted_index_to_json(inverted_index, 'gutenberg_inverted_index.json')

    # Step 9: Load the inverted index back from the JSON file
    loaded_inverted_index = load_inverted_index_from_json('gutenberg_inverted_index.json')

    # Step 10: Search for words in the loaded index
    search_word = "leaning"  # Example word to search for
    positions = search_word_in_index(search_word, loaded_inverted_index)
    
    if positions:
        print(f"Word '{search_word}' found at positions: {positions} ({len(positions)})")
    else:
        print(f"Word '{search_word}' not found.")