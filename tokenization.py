from bs4 import BeautifulSoup
import nltk
from writer import writeDict
from clean import extract_contexts_from_html


# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

def buildRawFreqVectors(html_file, contexts_file):
    # Abrir y leer el archivo HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read().lower()
    
    # Parsear el HTML usando BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text()
    
    # Tokenizar el texto
    tokens = nltk.word_tokenize(text)
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
    
    rawFreqVectorsDict = buildRawFreqVectors(html_file, contexts_file)
    writeDict(rawFreqVectorsDict, 'rawFrequencyVectors.txt')
