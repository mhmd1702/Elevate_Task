import googletrans
from googletrans import Translator

def translate_text():
    translator = Translator()

    print("---!Welcome to the Simple Language Translator!---")

    source_lang = input("Enter the source language code (e.g., 'en' for English): ").strip()
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ").strip()
    text_to_translate = input("Enter the text to translate: ")

    try:
        translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        print(f"Translated text: {translation.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    translate_text()
