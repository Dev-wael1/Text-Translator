import googletrans
import language_tool_python

# Initialize translator and grammar tool
translator = googletrans.Translator()
tool = language_tool_python.LanguageTool('en-US')  # For English grammar correction

def translate_text(text, target_language='en'):
    try:
        # Translate the text
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error in translation: {e}"

def correct_errors(text):
    # Correct grammatical errors
    corrected_text = tool.correct(text)
    return corrected_text

def translate_and_correct(text, target_language='en'):
    # Step 1: Translate the text
    translated_text = translate_text(text, target_language)
    
    # Step 2: Correct grammatical errors
    corrected_text = correct_errors(translated_text)
    
    return corrected_text

# Example Usage
input_text = "J'aime manger des pomme. il est trés bon"
target_language = 'en'  # Translate to English

# Translate and correct
result = translate_and_correct(input_text, target_language)
print("Translated and Corrected Text:", result)