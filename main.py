import requests
# pip3 install requests

# pip3 install nltk
import nltk
from nltk.corpus import stopwords


def word_count(str):
    # Maak een dictionary
    wordfreq = dict()

    # Kleine letters, zodat het beter te matchen is
    str_lower_case = str.lower()

    # Download de stopwoorden van nltk
    stop_words = set(stopwords.words('english'))

    # Maak een array van woorden van de tekst, dit is makkelijker loopen.
    words = str_lower_case.split()

    # Voor ieder woord in het array..
    for word in words:
        # Als het niet in de stopwoorden lijst staat
        if word not in stop_words:
            # ... als het al in de dict staat verhogen we de waarde ...
            if word in wordfreq:
                wordfreq[word] += 1
            # ... anders voegen we het woord toe en zetten we de waarde op 1
            else:
                wordfreq[word] = 1
    # Return de dictionary
    return wordfreq

# print(word_count("Een String om te testen of dit programma daadwerkelijk de keren dat een woord voorkomt telt. Volgens mij werkt dit prima. Laten we er een een een een groot tekst bestand insteken"))

# Dowload Frankenstein van Gutenberg project
url = 'http://www.gutenberg.org/files/84/84-0.txt'
output = requests.get(url).text

# Gooi het boek in de methode en sla de uitkomst op
verzameling = word_count(output)

# Organiseer de uitkomst op basis van hoe vaak het voorkomt en limiteer wat geprint wordt
index = 0
for word in sorted(verzameling, key=verzameling.get, reverse=True):
    if index < 100:
        print(word, verzameling[word])
        index += 1
    else: 
        break