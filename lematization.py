import stanza

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
        return word  # Si no se puede lematizar, se devuelve la palabra original
    
    return lemma

def lemmatize_frequency_vectors(file_path):
    lemmatized_freq_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Dividir la línea en palabras y descartar la frecuencia
            word = line.strip().split()[0]
            # Lematizar la palabra
            lemma = lemmatize_word(word)
            lemmatized_freq_dict[word] = lemma
    return lemmatized_freq_dict

# Archivo con el listado de palabras y frecuencias
raw_freq_file = 'rawFrequencyVectors.txt'

# Lematizar las palabras del archivo de frecuencia
lemmatized_freq_dict = lemmatize_frequency_vectors(raw_freq_file)

# Imprimir el diccionario de frecuencia lematizado
print("Diccionario de frecuencia lematizado:")
print(lemmatized_freq_dict)
