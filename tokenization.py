from bs4 import BeautifulSoup
import nltk
from writer import writeDict

def get_contexts_from_file(contexts_file):
    contexts = {}
    with open(contexts_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # Eliminar espacios en blanco adicionales
            if line:
                parts = line.split()  # Separar la línea en palabras
                word = parts[0]  # La primera palabra es la palabra clave
                context = parts[1:]  # El resto de las palabras son el contexto
                contexts[word] = context  # Agregar el contexto al diccionario
    return contexts

def buildRawFreqVectors(contexts):
    # Obtener todas las palabras únicas de los contextos
    vocabulary = list(set(word for context in contexts.values() for word in context))

    rawFreqVectorsDict = {}

    # Inicializar los vectores de frecuencia
    for word in vocabulary:
        rawFreqVectorsDict[word] = [0] * len(vocabulary)

    # Calcular la frecuencia de cada palabra en todos los contextos
    for context in contexts.values():
        for word in vocabulary:
            rawFreqVectorsDict[word][vocabulary.index(word)] += context.count(word)

    return rawFreqVectorsDict


def getContext(vocabTokenizado, palabra, contextos=False):    
    context_left = []
    context_right = []
    for i in range(len(vocabTokenizado)):
        if vocabTokenizado[i] == palabra:
            left = ' '.join(vocabTokenizado[max(0, i-8):i])
            right = ' '.join(vocabTokenizado[i+1:min(i+9, len(vocabTokenizado))])
            context_left.append(left)
            context_right.append(right)
    if contextos:
        return context_left, context_right
    else:
        return "Contextos izquierdos: {}\nContextos derechos: {}".format(context_left, context_right)

if __name__ == '__main__':
    html_file = 'e990624_mod.htm'
    contexts_file = 'contexts.txt'
    
    # Obtener contextos del archivo de texto
    contexts = get_contexts_from_file(contexts_file)
    
    # Construir vectores de frecuencia a partir de los contextos
    rawFreqVectorsDict = buildRawFreqVectors(contexts)
    
    # Escribir los vectores de frecuencia en el archivo 'rawFrequencyVectors.txt'
    writeDict(rawFreqVectorsDict, 'rawFrequencyVectors.txt')
   