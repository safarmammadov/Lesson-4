from translate import Translator
from translate import Translator
translator= Translator(to_lang="zh")
print ('Фира прошу внеси слова на английском языке')
WORD = (input())
print (translator.translate(WORD))






