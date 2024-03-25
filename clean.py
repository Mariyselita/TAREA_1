import re
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def clean_html_tags(html_text):
    # Eliminar etiquetas HTML
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    
    # Eliminar caracteres especiales utilizando expresiones regulares
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convertir el texto a minúsculas
    text = text.lower()
    
    # Tokenizar el texto
    tokens = nltk.word_tokenize(text)
    
    # Obtener stopwords en español
    stop_words = set(stopwords.words('spanish'))
    
    # Filtrar stopwords y contar tokens limpios y stopwords
    clean_tokens = []
    stopwords_removed = 0
    for token in tokens:
        if token not in stop_words:
            clean_tokens.append(token)
        else:
            stopwords_removed += 1
    
    # Contar palabras en el vocabulario
    vocabulary_size = len(set(clean_tokens))
    
    # Unir los tokens filtrados en un texto limpio
    clean_text = ' '.join(clean_tokens)
    
    return clean_text, len(clean_tokens), stopwords_removed, vocabulary_size

def extract_contexts_from_html(html_file, contexts_file):
    # Abrir y leer el archivo HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_text = f.read()
    
    # Limpiar el texto HTML para eliminar etiquetas, caracteres especiales y stopwords
    cleaned_text, total_tokens, stopwords_removed, vocabulary_size = clean_html_tags(html_text)
    
    # Dividir el texto en palabras y extraer contextos
    words = cleaned_text.split()
    num_words = len(words)
    
    # Escribir los contextos en el archivo
    with open(contexts_file, 'w', encoding='utf-8') as f:
        for i, word in enumerate(words):
            if i < num_words - 1:
                context = ' '.join(words[i+1:i+6])  # Tomar las siguientes 5 palabras como contexto
                f.write(f"{word} {context}\n")
    
    print("Total de tokens limpios:", total_tokens)
    print("Número de stopwords eliminadas:", stopwords_removed)
    print("Número de palabras en el vocabulario:", vocabulary_size)
    print(f"Contextos extraídos del archivo {html_file} y escritos en {contexts_file}.")

if __name__ == '__main__':
    html_file = 'e990624_mod.htm'
    contexts_file = 'contexts.txt'
    
    extract_contexts_from_html(html_file, contexts_file)
