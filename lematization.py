import stanza
from collections import Counter
from nltk.corpus import stopwords
import re

# Descargar el conjunto de stopwords en español
import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

# Inicializar el procesador de CoreNLP para español
nlp = stanza.Pipeline('es')

def lemmatize_word(word):
    # Procesar la palabra para lematización
    doc = nlp(word)
    
    # Obtener el lema de la palabra
    lemma = None
    for sent in doc.sentences:
        for token in sent.tokens:
            if token.words:
                lemma = token.words[0].lemma
                break
    
    if not lemma:
        print(f"No se pudo lematizar la palabra '{word}'")
        return word, word  # Si no se puede lematizar, se devuelve la palabra original
    
    return word, lemma

def lemmatize_frequency_vectors(file_path):
    lemmatized_freq_dict = {}
    original_lemmas = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Dividir la línea en palabras y descartar la frecuencia
            word = line.strip().split()[0]
            # Lematizar la palabra
            word, lemma = lemmatize_word(word)
            lemmatized_freq_dict[word] = lemma
            original_lemmas[word] = lemma
    return lemmatized_freq_dict, original_lemmas

def preprocess_text(text):
    # Convertir el texto a minúsculas
    text = text.lower()
    # Eliminar caracteres especiales y números
    text = re.sub(r'[^a-záéíóúüñ]', ' ', text)
    return text

# Archivo con el listado de palabras y frecuencias
raw_freq_file = 'rawFrequencyVectors.txt'

# Lematizar las palabras del archivo de frecuencia
lemmatized_freq_dict, original_lemmas = lemmatize_frequency_vectors(raw_freq_file)

# Imprimir el diccionario de frecuencia lematizado en vertical
print("Diccionario de frecuencia lematizado:")
for word, lemma in lemmatized_freq_dict.items():
    print(f"{word}: {lemma}")

# Texto antes de lematización
print("\nTexto antes de lematización:")
with open('contexts.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()
print(original_text[:200])  # Mostrar solo los primeros 200 caracteres
print("Longitud:", len(original_text))

# Lematizar el texto
processed_text = preprocess_text(original_text)
lemmatized_text = ' '.join([lemmatize_word(word)[1] for word in processed_text.split()])

# Texto después de lematización
print("\nTexto después de lematización:")
print(lemmatized_text[:200])  # Mostrar solo los primeros 200 caracteres
print("Longitud:", len(lemmatized_text))

# Eliminar stopwords del texto lematizado
lemmatized_text_without_stopwords = ' '.join([word for word in lemmatized_text.split() if word not in stop_words])

# Texto sin stopwords después de lematizar
print("\nTexto sin stopwords después de lematizar:")
print(lemmatized_text_without_stopwords[:200])  # Mostrar solo los primeros 200 caracteres

# Contar las palabras similares en texto sin lematizar
word_counter = Counter(processed_text.split())
similar_words_count = sum([word_counter[word] for word in lemmatized_text.split() if word in word_counter])

print("\nTotal de palabras similares en texto sin lematizar:", similar_words_count)
