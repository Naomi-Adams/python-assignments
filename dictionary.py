import json
import difflib

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return json.load(file)
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return None
    
def suggest_word(word, dictionary):
    words = dictionary.keys()
    suggestions = difflib.get_close_matches(word, words)
    return suggestions[0] if suggestions else None
def find_definition(word,dictionary.json):    
    definition = get_definition(word,dictionary.json)
    if definition:
        return definition
    else:
        suggestion = suggest_word(word, dictionary.json)
        if suggestion:
            return f"Word not found. Did you mean '{suggestion}'? Definition: {dictionary[suggestion]}"
        else:
            return "Word not found and no suggestions available"
        
def main():
    dictionary = load_dictionary('dictionary.json')
    while True:
        user_input = input("Enter a word to define (or 'exit' to quit): ").strip()
        if user_input.lower() =='exit':
            break
        print(get_definition)
        
if __name__=="_main_":
    main