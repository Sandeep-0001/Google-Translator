from googletrans import Translator

translator = Translator()
txt = input("Enter the sentence which you want to translate:\n")
output = translator.translate(txt, dest='en')
print(output.text)
