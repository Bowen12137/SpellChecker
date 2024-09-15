import datetime
import os
import json
from difflib import SequenceMatcher


class SpellCheckerTranslator:
    def __init__(self, dictionary_file="EnglishWords.txt", translation_file="data.json"):
        # Load the dictionary and translation data when the class is initialized
        self.dictionary = self.load_dictionary(dictionary_file)
        self.translation_data = self.load_translation_data(translation_file)

    def load_dictionary(self, file_path):
        """Loads the dictionary of valid English words from a file."""
        try:
            with open(file_path) as file:
                # Load the file and convert each line to lowercase and strip whitespace
                return {line.strip().lower() for line in file}
        except FileNotFoundError:
            # Handle case where the dictionary file is not found
            print(f"Dictionary file '{file_path}' not found.")
            return set()  # Return an empty set if the file is missing

    def load_translation_data(self, file_path):
        """Loads the translation data from a JSON file."""
        try:
            with open(file_path) as file:
                # Load the JSON data and return it as a Python dictionary
                return json.load(file)
        except FileNotFoundError:
            # Handle case where the translation file is not found
            print(f"Translation file '{file_path}' not found.")
            return {}

    def clean_word(self, word):
        """Removes non-alphabetical characters from a word."""
        # Filter out non-alphabetical characters and return a clean version of the word
        return ''.join([letter for letter in word if letter.isalpha()])

    def translate(self, word):
        """Translates a word if it exists in the translation data."""
        # Look up the word in the translation data and return the meaning
        # If no translation is found, return a default message
        return self.translation_data.get(word, f"No translation found for '{word}'")

    def suggest_correction(self, word):
        """Suggests a correction for a misspelled word using the closest match."""
        # Find the best match for a word by comparing it with the dictionary using SequenceMatcher
        best_match = max(self.dictionary, key=lambda dict_word: SequenceMatcher(None, word, dict_word).ratio())
        return best_match

    def spellcheck_word(self, word):
        """Checks if the word is in the dictionary."""
        # Clean the word by removing non-alphabetical characters
        alpha_word = self.clean_word(word.lower())
        if not alpha_word:
            # Skip if the word is empty or doesn't contain letters
            return None, False, None

        if alpha_word in self.dictionary:
            # If the word is in the dictionary, it's spelled correctly
            return alpha_word, True, None
        else:
            # If the word isn't found, suggest a correction
            return alpha_word, False, self.suggest_correction(alpha_word)

    def spellcheck_sentence(self, sentence):
        """Spellchecks a sentence provided by the user."""
        words = sentence.split()  # Split the sentence into words
        count_correct, count_not_correct = 0, 0  # Counters for correct and incorrect words

        print("┌───────────────────────────────────────────────────────┐")
        for word in words:
            # Spellcheck each word
            alpha_word, correct, suggestion = self.spellcheck_word(word)

            if alpha_word:
                if correct:
                    # Print if the word is spelled correctly
                    print(f"│ {alpha_word} (spelt correctly)")
                    count_correct += 1
                else:
                    # Print the word and suggest a correction if it is incorrect
                    print(f"│ {alpha_word} not found in dictionary. Did you mean '{suggestion}'?")
                    count_not_correct += 1
        print("└───────────────────────────────────────────────────────┘")

        # Print the summary of results
        self.print_summary(len(words), count_correct, count_not_correct)

    def spellcheck_file(self, file_path):
        """Spellchecks a file provided by the user."""
        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"File '{file_path}' not found.")
            return

        # Read the content of the file
        with open(file_path) as file:
            text = file.read().lower()

        # Spellcheck the file's content
        self.spellcheck_sentence(text)

    def check_word_meaning(self, word):
        """Checks the meaning (translation) of a single word."""
        # Clean the word to remove non-alphabetical characters
        alpha_word = self.clean_word(word.lower())
        if alpha_word in self.translation_data:
            # If the word exists in the translation data, print its meaning(s)
            meanings = self.translation_data[alpha_word]
            print(f"┌─────────────────────────────┐")
            print(f"│ Meaning of '{alpha_word}':    │")
            print(f"└─────────────────────────────┘")
            for idx, meaning in enumerate(meanings, 1):
                print(f"  {idx}. {meaning}")
            print("───────────────────────────────")
        elif alpha_word in self.dictionary:
            # If the word is in the dictionary but no meaning is found
            print(f"┌─────────────────────────────┐")
            print(f"│ '{alpha_word}' is a valid word, but no meaning found. │")
            print(f"└─────────────────────────────┘")
        else:
            # If the word is not found in the dictionary, suggest a correction
            suggestion = self.suggest_correction(alpha_word)
            print(f"┌───────────────────────────────────────────────────┐")
            print(f"│ Word '{alpha_word}' not found in dictionary.       │")
            print(f"│ Did you mean '{suggestion}'?                        │")
            print(f"└───────────────────────────────────────────────────┘")

    def print_summary(self, count_words, count_correct, count_not_correct):
        """Prints a summary of spellchecking results."""
        # Print the total number of words, correct words, and incorrect words
        print("┌──────────────────────────────────────────────────────────────────────────┐")
        print(f"│ Number of words: {count_words}")
        print(f"│ Number of correctly spelt words: {count_correct}")
        print(f"│ Number of incorrectly spelt words: {count_not_correct}")
        print("└──────────────────────────────────────────────────────────────────────────┘")

    def run_menu(self):
        """Main menu for the spellchecker and translator."""
        # Continuously display the menu and process user input
        while True:
            print("┌──────────────────────────────┐")
            print("│ Spell Checker & Translator   │")
            print("│ 1. Check a file              │")
            print("│ 2. Check a sentence          │")
            print("│ 3. Check word meaning        │")
            print("│ 0. Quit                      │")
            print("└──────────────────────────────┘")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Prompt for file path and spellcheck the file
                file_path = input("Enter file path to spellcheck: ")
                self.spellcheck_file(file_path)
            elif choice == "2":
                # Prompt for a sentence and spellcheck the sentence
                sentence = input("Enter sentence to spellcheck: ")
                self.spellcheck_sentence(sentence)
            elif choice == "3":
                # Prompt for a word and check its meaning
                word = input("Enter a word to check the meaning: ")
                self.check_word_meaning(word)
            elif choice == "0":
                # Exit the program
                print("Goodbye!")
                break
            else:
                # Handle invalid input
                print("Invalid input. Please select either 1, 2, 3, or 0.")


# If this script is run as the main program, initialize the spell checker and run the menu
if __name__ == "__main__":
    spell_checker_translator = SpellCheckerTranslator()
    spell_checker_translator.run_menu()
