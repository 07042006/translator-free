from googletrans import Translator
translator = Translator()

#lista = ['Olá, tudo bem?', 'Bom dia', 'Eu tenho um cachorro.']

#try:
    #translations = translator.translate(lista, dest='ko')
    #for translation in translations:
        #print(translation.text)
#except Exception as e:
    #print(e)

translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='pt')
print(translation.text)