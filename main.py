from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def main():
    # Read the source text from source.txt
    with open('source.txt', 'r') as file:
        source_text = file.read().strip()

    # Set the source and target languages
    source_lang = 'en'  # Assuming the source text is in English
    target_lang = 'fr'  # Assuming the target language is French

    # Translate the text
    translated_text = translate_text(source_text, source_lang, target_lang)
    print(translated_text)

if __name__ == '__main__':
    main()
