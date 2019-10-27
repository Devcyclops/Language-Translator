from googletrans import Translator
translator = Translator()
def Translate():
    word = input('enter the word you want to translate to: ')
    print("enter the short form of the language you want to translate to eg: en=english, ch=chinese, ko=korean etc")
    destination = input('what language do you want to translate to: ') 
    translated_word = translator.translate(word, destination).text
    print(translated_word)
    
Translate()    

          
