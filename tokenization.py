from bs4 import BeautifulSoup
import nltk
from writer import writeDict
from clean import clean_html_tags, extract_contexts_from_html

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

def buildRawFreqVectors(html_file, contexts_file):
    # Limpiar el HTML y obtener tokens limpios
    cleaned_text, _, _, _ = clean_html_tags(html_file)
    
    # Tokenizar el texto limpio
    tokens = nltk.word_tokenize(cleaned_text)
    vocabulary = list(set(tokens))
    
    rawFreqVectorsDict = {}
    
    # Leer los contextos del archivo de texto y procesarlos
    with open(contexts_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # Eliminar espacios en blanco adicionales
            if line:
                parts = line.split()  # Separar la línea en palabras
                word = parts[0]  # La primera palabra es la palabra clave
                context = parts[1:]  # El resto de las palabras son el contexto
                vector = [context.count(word) for word in vocabulary]  # Construir el vector de frecuencia
                rawFreqVectorsDict[word] = vector  # Agregar el vector al diccionario
    
    return rawFreqVectorsDict

if __name__ == '__main__':
    html_file = 'e990624_mod.htm'
    contexts_file = 'contexts.txt'
    
    # Extraer contextos del archivo HTML y escribirlos en el archivo 'contexts.txt'
    extract_contexts_from_html(html_file, contexts_file)
    
    # Construir vectores de frecuencia a partir de los contextos
    rawFreqVectorsDict = buildRawFreqVectors(html_file, contexts_file)
    
    # Escribir los vectores de frecuencia en el archivo 'rawFrequencyVectors.txt'
    writeDict(rawFreqVectorsDict, 'rawFrequencyVectors.txt')
