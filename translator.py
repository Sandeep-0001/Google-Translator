from googletrans import Translator,LANGUAGES

translator = Translator()
txt = input("Enter the word/sentence which you want to translate:\n")
output = translator.translate(txt, dest='en')


print("\nTranslation Result:")
print("Original Text:", txt)
print("Detected Language:", LANGUAGES[output.src].capitalize())  
print("Translated Text:", output.text)
