from deep_translator import GoogleTranslator

langs_list = GoogleTranslator().get_supported_languages() 
print(langs_list)