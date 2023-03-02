#Vamos a importar librerias
import spacy
from spacy import displacy
from spacy.lang.es.stop_words import STOP_WORDS 

#STOP_WORDS.add("")#Agregar una nueva palabra a nuestro stop_words

nlp = spacy.load('es_core_news_sm')#Vamos a cargar el core_news_sm ya que nos sirve para analizar y procesar datos
#Creamos una variable de texto y pedir al usuario ingresar datos
txt1 = str(input("Escribir una frase: "))
Respuesta = []
ind = 0
palabras = nlp.create_pipe('sentencizer') #esto nos sirve para hacer la separacion de cada palabra en la oracion

#con nlp vamos a procesar el txt1 para identificar las palabras por separado
doc = nlp(txt1)   

#Aqui vamos hacer el filtrado de la oracion 
for token in doc:
    temp = str(token.pos_)
    tokentemp = str(token.text)
    if temp == "NOUN":
        if tokentemp == "idiota":
           token = "******"
    Palabra = str(token)
    Respuesta.insert(ind, Palabra)
    ind = ind + 1
    temp = ''
    tokentemp = ''

print("La frase filtrada es: ", *Respuesta)

    