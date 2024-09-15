

# SpellChecker & Translator

`SpellChecker & Translator` is a comprehensive tool that allows users to check the spelling of words in a sentence or file, retrieve word definitions, and get suggestions for misspelled words. It utilizes a combination of a word dictionary (`EnglishWords.txt`) for spell checking and a word definition database (`data.json`) for word meanings. This interactive tool is built with a user-friendly interface, making it accessible for a variety of tasks.

![Badge](https://img.shields.io/badge/version-1.0.0-blue) ![Badge](https://img.shields.io/badge/python->=3.6-green)

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Contact & Feedback](#contact--feedback)

## Features
- **Sentence Spell Checking**: Quickly checks the spelling of each word in a given sentence and suggests corrections for misspelled words.
- **File Spell Checking**: Processes an entire file to check the spelling of each word.
- **Word Suggestions**: For any misspelled word, it suggests the closest possible correction based on word similarity using the `SequenceMatcher`.
- **Word Definitions**: Retrieves the definition or translation of any word from an integrated `data.json` dictionary. If no definition is found, the user is notified.
- **Correction Suggestions**: Provides suggestions for any misspelled word.
- **Interactive Menu**: Offers an easy-to-use menu interface for users to navigate through the tool's various functionalities.

## Requirements
- **Python 3.6 or newer**: The tool is built using Python 3.6+.
- **Files**:
  - `EnglishWords.txt`: A file containing valid English dictionary words, one word per line.
  - `data.json`: A JSON file containing word definitions or translations. The structure should have each word as a key and its definition(s) as a list of strings, like so:
  
    ```json
    {
      "example": ["A representative form or pattern", "An instance of something"],
      "abandoned industrial site": ["Site that cannot be used for any purpose, being contaminated by pollutants."]
    }
    ```

## Installation
1. **Clone the repository** or download the `SpellCheckerTranslator.py` file.
   ```bash
   git clone https://github.com/your-username/spellchecker.git
   cd spellchecker
   ```
2. **Prepare the required files**:
   - Make sure you have `EnglishWords.txt` (a file containing dictionary words) and `data.json` (containing word definitions or translations).
   - Place these files in the same directory as the `SpellCheckerTranslator.py` script.

3. **Run the Program**:
   Run the program from the terminal using:
   ```bash
   python SpellCheckerTranslator.py
   ```

## Usage

Once the program starts, you will be greeted with a menu. The options available are:

1. **Check a File**: 
   - Input a file path, and the tool will check the spelling of all words in the file, suggesting corrections for misspelled words.
   - Example:
     ```plaintext
     ┌──────────────────────────────┐
     │ Spell Checker & Translator   │
     │ 1. Check a file              │
     │ 2. Check a sentence          │
     │ 3. Check word meaning        │
     │ 0. Quit                      │
     └──────────────────────────────┘
     ```

2. **Check a Sentence**:
   - Enter a sentence, and the tool will spellcheck each word and provide suggestions for any incorrect words.

3. **Check Word Meaning**:
   - Enter a single word, and the tool will return its definition or translation from `data.json`.
   - Example:
     ```plaintext
     ┌──────────────────────────────┐
     │ Meaning of 'example':         │
     └──────────────────────────────┘
      1. A representative form or pattern
      2. An instance of something
     ```

4. **Quit**: Exit the program.

### Command-Line Example:
```bash
$ python SpellCheckerTranslator.py
┌──────────────────────────────┐
│ Spell Checker & Translator   │
│ 1. Check a file              │
│ 2. Check a sentence          │
│ 3. Check word meaning        │
│ 0. Quit                      │
└──────────────────────────────┘
Enter your choice: 2
Enter sentence to spellcheck: I am runing fast
│ am (spelt correctly)
│ runing not found in dictionary. Did you mean 'running'?
│ fast (spelt correctly)
```

## Contribution Guidelines
We welcome contributions to enhance the functionality of the `SpellChecker & Translator`. Here's how you can contribute:

1. **Fork the repository**.
2. **Create a feature branch** for your feature or bug fix.
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Make the necessary changes** and commit them.
   ```bash
   git commit -m "Add feature: your-feature"
   ```
4. **Push the changes** to your fork.
   ```bash
   git push origin feature/your-feature
   ```
5. **Submit a pull request** to merge your changes into the main repository.

For major changes, please open an issue first to discuss what you would like to change. Be sure to include tests where applicable.

## License
This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact & Feedback
We highly appreciate any feedback and suggestions. If you have questions or encounter issues, feel free to reach out via email:

✉️ **Email**: Arthur12137@gmail.com
```

You can copy this markdown and use it as your `README.md` file. This version provides a detailed overview, setup instructions, and usage examples for your project.
