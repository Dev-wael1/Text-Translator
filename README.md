
# Text Translator and Error Corrector

This is a simple Python project that performs two main tasks:
1. **Translates text**: Uses the Google Translate API to translate text from any language to a specified target language.
2. **Corrects grammatical errors**: Uses the LanguageTool library to identify and correct grammar and spelling mistakes in the translated text.

## Features
- Supports translation to multiple languages.
- Corrects grammatical errors in the translated text.
- Easy to use and extend.

## Requirements

Before you start, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository or download the code:
   ```bash
   git clone https://github.com/Dev-wael1/Text-Translator.git
   cd Text-Translator
   ```

2. Install the required Python libraries:
   ```bash
   pip install googletrans==4.0.0-rc1 language-tool-python
   ```

## Usage

1. Import the required libraries and functions:

   ```python
   import googletrans
   import language_tool_python
   ```

2. Use the provided functions to translate and correct text. Here’s an example:

   ```python
   input_text = "J'aime manger des pomme. il est trés bon"
   target_language = 'en'  # Translate to English

   result = translate_and_correct(input_text, target_language)
   print("Translated and Corrected Text:", result)
   ```

### Example Output:

Input (French):
```
J'aime manger des pomme. il est trés bon
```

Output (English and corrected):
```
I like eating apples. It is very good.
```

## Functions

### `translate_text(text, target_language='en')`
Translates the given text into the target language using Google Translate.

- **text**: The input text to be translated.
- **target_language**: The language to translate the text into (default: English `'en'`).

### `correct_errors(text)`
Corrects any grammatical errors in the given text using LanguageTool.

- **text**: The input text to be checked for grammar errors.

### `translate_and_correct(text, target_language='en')`
A combination of translation and error correction. It first translates the text and then applies grammar corrections.

- **text**: The input text.
- **target_language**: The language to translate the text into (default: English `'en'`).

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Google Translate API](https://pypi.org/project/googletrans/)
- [LanguageTool](https://github.com/jxmorris12/language_tool_python)
```