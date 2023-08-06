from googleapiclient import discovery
from googleapiclient.errors import HttpError
import json
import time
import gzip
import os
import random

# Hier muss der API-Key für Perspective eingefügt werden.
# Achtung! Teilt euren API-Key nicht öffentlich!
API_KEY = ''

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
  )

tweets = []

# Diese Funktion durchsucht alle Tweet-Dateien im aktuellen Ordner und deren
# Unterordnern und gibt sie als Array zurück
def find_all_json_gz_files(root_folder):
    json_gz_files = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        print("Durchsuche Ordner: ", foldername)
        for filename in filenames:
            if filename.endswith('.json.gz'):
                json_gz_files.append(os.path.join(foldername, filename))
                print("Gefunden: ", filename)
    return json_gz_files

# Diese Funktion wählt eine Anzahl (num_files_to_read) an zufälligen Dateien
# der Tweet-Dateien aus und fügt die enthaltenen Tweets einem Array hinzu (tweets)
# Zusätzlich wird eine Text-Datei enthält, in der gespeichert wird, welche
# Dateien ausgewählt wurden
def read_random_json_gz_files(file_list, num_files_to_read):
    selected_files = random.sample(file_list, num_files_to_read)
    with open('selected_files.txt', 'w') as txt_file:
        for file_path in selected_files:
            txt_file.write(file_path + '\n')
            print("Die Datei ", file_path, "wurde ausgewählt.")
            time.sleep(2)

    for file_path in selected_files:
         with gzip.open(file_path, 'r') as file:
             for line in file:
                 tweets.append(json.loads(line))

# Hier wird der Pfad des Hauptordners angegeben. Der Punkt sagt, dass der
# Hauptordner der Pfad sein soll, in der diese Python-Datei liegt
root_folder_path = '.'
# Hier wird angegeben, wie viele Tweet-Dateien ausgewählt werden sollen.
# Eine Tweet-Datei enthält ungefähr 2000 Tweets
num_files_to_read = 5

print("Aktuelles Arbeitsverzeichnis: ", os.getcwd())

all_json_gz_files = find_all_json_gz_files(root_folder_path)
if len(all_json_gz_files) < num_files_to_read:
    print("Es gibt weniger als 5 .json.gz-Dateien in der Ordnerstruktur.")
else:
     read_random_json_gz_files(all_json_gz_files, num_files_to_read)
     # Öffnen bzw. Anlegen der JSON zum Speichern der Analyseergebnisse
     with open('analyzed_tweets.json', 'w') as output_file:
         output_file.write("[")
         output_file.write('\n')
         # Iterieren über die Tweets
         for index, tweet in enumerate(tweets, start=1):

             print("Analysiere Tweet ", index, " von ", len(tweets))
             # Zugriff auf den Text des Tweets
             tweet_text = tweet['text']

             try:
                 # Ab hier werden die Tweets zur Perspective-API geschickt
                 # und auf die angegebenen Attribute analyisiert.
                 analyze_request = {
                     'comment': {'text': tweet_text},
                     'requestedAttributes': {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'IDENTITY_ATTACK': {}, 'INSULT': {}, 'PROFANITY': {}, 'THREAT': {}}
                     }

                 response = client.comments().analyze(body=analyze_request).execute()

                 output_file.write(json.dumps(response, indent=2))
                 if index < len(tweets):
                     output_file.write(",")
                 output_file.write('\n')

             except HttpError as error:
                 if error.resp.status == 400 and "LANGUAGE_NOT_SUPPORTED_BY_ATTRIBUTE" in str(error):
                     # Wenn ein Tweet eine nicht unterstützte Sprache hat, wird
                     # mit dem nächsten Tweet weitergemacht
                     continue
                 else:
                     # Zur Sicherheit, falls noch andere Fehler auftreten
                     raise error
             time.sleep(2)

             print(json.dumps(response, indent=2))

             if index == len(tweets):
                 output_file.write("]")
                 break
