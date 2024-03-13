from translate import Translator


translator = Translator(from_lang='spanish',to_lang='english')

txt = input("Ingrese el texto a traducir >>>   ")

res = translator.translate(txt)

print(res)



