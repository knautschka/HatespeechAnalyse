import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

stichproben = ['Dezember 2021', 'November 2022']

# Analysedaten auslesen
data_2021 = []

with open('zusammenfassung_2021.txt', 'r') as file:
    for line in file:
        columns = line.strip().split()  # Teilt die Zeile in Spalten
        if columns and columns[0].isdigit():  # Überprüft, ob die Zeile nicht leer ist
            data_2021.append(int(columns[0]))  # Fügt den ersten Wert der Zeile zur Liste hinzu

# data_2021 enthält jetzt die Daten aus der ersten Spalte des .txt-Dokuments
print(data_2021)

data_2022 = []

with open('zusammenfassung_2022.txt', 'r') as file:
    for line in file:
        columns = line.strip().split()  # Teilt die Zeile in Spalten
        if columns and columns[0].isdigit():  # Überprüft, ob die Zeile nicht leer ist
            data_2022.append(int(columns[0]))  # Fügt den ersten Wert der Zeile zur Liste hinzu

print(data_2022)

general_hatespeech_tweets_2021 = [data_2021[0], data_2021[1]]
general_hatespeech_tweets_2022 = [data_2022[0], data_2022[1]]

observed_general_hatespeech_2021 = np.array(general_hatespeech_tweets_2021)
observed_general_hatespeech_2022 = np.array(general_hatespeech_tweets_2022)

contingency_table_general_hatespeech = pd.DataFrame({'Dezember 2021': observed_general_hatespeech_2021, 'November 2022': observed_general_hatespeech_2022})

chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table_general_hatespeech)

alpha = 0.01

p_val_formatted = '{:.10f}'.format(p_val)
general_hatespeech_p = p_val_formatted

if p_val < alpha:
    print("Es gibt einen statistisch signifikanten Unterschied zwischen Dezember 2021 und November 2022. Der p-Wert beträgt ", p_val_formatted)
else:
    print("Es gibt keinen statistisch signifikanten Unterschied zwischen Dezember 2021 und November 2022. Der p-Wert beträgt ", p_val_formatted)

tweet_count_2021 = general_hatespeech_tweets_2021[0] + general_hatespeech_tweets_2021[1]
tweet_count_2022 = general_hatespeech_tweets_2022[0] + general_hatespeech_tweets_2022[1]

no_hatespeech_2021_percent = (general_hatespeech_tweets_2021[0] / tweet_count_2021) * 100
no_hatespeech_2022_percent = (general_hatespeech_tweets_2022[0] / tweet_count_2022) * 100
hatespeech_2021_percent = (general_hatespeech_tweets_2021[1] / tweet_count_2021) * 100
hatespeech_2022_percent = (general_hatespeech_tweets_2022[1] / tweet_count_2022) * 100

kategorien = ('Kein Hatespeech \nDezember 2021', 'Kein Hatespeech \nNovember 2022', 'Hatespeech \nDezember 2021', 'Hatespeech \nNovember 2022')
werte = [no_hatespeech_2021_percent, no_hatespeech_2022_percent, hatespeech_2021_percent, hatespeech_2022_percent]
farben = ['blue', 'orange', 'blue', 'orange']

y_pos = np.arange(len(kategorien))
plt.bar(y_pos, werte, align='center', color=farben)
plt.xticks(y_pos, kategorien)
plt.ylabel('Verteilung in Prozent')
plt.title('Generelles Hatespeech-Vorkommen Dezember 2021 / November 2022')
plt.savefig('vergleich_genereller_hatespeech_diagramm.png')
plt.show()

# Daten der einzelnen Kategorien vorbereiten
toxicity_2021 = [data_2021[2], data_2021[3], data_2021[4], data_2021[5], data_2021[6]]
toxicity_2022 = [data_2022[2], data_2022[3], data_2022[4], data_2022[5], data_2022[6]]

severe_toxicity_2021 = [data_2021[7], data_2021[8], data_2021[9], data_2021[10], data_2021[11]]
severe_toxicity_2022 = [data_2022[7], data_2022[8], data_2022[9], data_2022[10], data_2022[11]]

identity_attack_2021 = [data_2021[12], data_2021[13], data_2021[14], data_2021[15], data_2021[16]]
identity_attack_2022 = [data_2022[12], data_2022[13], data_2022[14], data_2022[15], data_2022[16]]

insult_2021 = [data_2021[17], data_2021[18], data_2021[19], data_2021[20], data_2021[21]]
insult_2022 = [data_2022[17], data_2022[18], data_2022[19], data_2022[20], data_2022[21]]

profanity_2021 = [data_2021[22], data_2021[23], data_2021[24], data_2021[25], data_2021[26]]
profanity_2022 = [data_2022[22], data_2022[23], data_2022[24], data_2022[25], data_2022[26]]

threat_2021 = [data_2021[27], data_2021[28], data_2021[29], data_2021[30], data_2021[31]]
threat_2022 = [data_2022[27], data_2022[28], data_2022[29], data_2022[30], data_2022[31]]

def berechne_p_und_erstelle_diagramm(data_for_2021, data_for_2022, xlabel, title, filename):
    observed_2021 = np.array(data_for_2021)
    observed_2022 = np.array(data_for_2022)

    contingency_table = pd.DataFrame({'Dezember 2021': observed_2021, 'November 2022': observed_2022})

    chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)

    alpha = 0.01

    p_val_formatted = '{:.10f}'.format(p_val)

    if p_val < alpha:
        print("Es gibt einen statistisch signifikanten Unterschied zwischen Dezember 2021 und November 2022. Der p-Wert beträgt ", p_val_formatted)
    else:
        print("Es gibt keinen statistisch signifikanten Unterschied zwischen Dezember 2021 und November 2022. Der p-Wert beträgt ", p_val_formatted)

    observed_2021_019_percent = (observed_2021[0] / tweet_count_2021) * 100
    observed_2021_2049_percent = (observed_2021[1] / tweet_count_2021) * 100
    observed_2021_5069_percent = (observed_2021[2] / tweet_count_2021) * 100
    observed_2021_7089_percent = (observed_2021[3] / tweet_count_2021) * 100
    observed_2021_90100_percent = (observed_2021[4] / tweet_count_2021) * 100

    observed_2022_019_percent = (observed_2022[0] / tweet_count_2022) * 100
    observed_2022_2049_percent = (observed_2022[1] / tweet_count_2022) * 100
    observed_2022_5069_percent = (observed_2022[2] / tweet_count_2022) * 100
    observed_2022_7089_percent = (observed_2022[3] / tweet_count_2022) * 100
    observed_2022_90100_percent = (observed_2022[4] / tweet_count_2022) * 100

    kategorien = ['0-19 %', '20-49 %', '50-69 %', '70-89 %', '90-100 %']
    values_2021 = [observed_2021_019_percent, observed_2021_2049_percent, observed_2021_5069_percent, observed_2021_7089_percent, observed_2021_90100_percent]
    values_2022 = [observed_2022_019_percent, observed_2022_2049_percent, observed_2022_5069_percent, observed_2022_7089_percent, observed_2022_90100_percent]

    num_categories = len(kategorien)
    x = np.arange(num_categories)
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values_2021, width, label='Dezember 2021')
    rects2 = ax.bar(x + width/2, values_2022, width, label='November 2022')
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Verteilung in Prozent')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(kategorien)
    ax.legend()
    plt.savefig(filename)
    plt.show()

    return p_val_formatted


toxicity_p = berechne_p_und_erstelle_diagramm(toxicity_2021, toxicity_2022, 'Toxizitätswahrscheinlichkeit', 'Vergleich der Toxizitätsverteilung Dezember 2021 und November 2022', 'vergleich_toxizitaet_diagramm.png')
severe_toxicity_p = berechne_p_und_erstelle_diagramm(severe_toxicity_2021, severe_toxicity_2022, 'Schwere Toxizitätswahrscheinlichkeit', 'Schwere Toxizitätsverteilung Dezember 2021 und November 2022', 'vergleich_schwere_toxizitaet_diagramm.png')
identity_attack_p = berechne_p_und_erstelle_diagramm(identity_attack_2021, identity_attack_2022, 'Identitätsangriffswahrscheinlichkeit', 'Identitätsangriffsverteilung Dezember 2021 und November 2022', 'vergleich_identitaetsangriff_diagramm.png')
insult_p = berechne_p_und_erstelle_diagramm(insult_2021, insult_2022, 'Beleidigungswahrscheinlichkeit', 'Beleidigungsverteilung Dezember 2021 und November 2022', 'vergleich_beleidigung.png')
profanity_p = berechne_p_und_erstelle_diagramm(profanity_2021, profanity_2022, 'Obszönitätswahrscheinlichkeit', 'Obszönitätsverteilung Dezember 2021 und November 2022', 'vergleich_obszoenitaet.png')
threat_p = berechne_p_und_erstelle_diagramm(threat_2021, threat_2022, 'Bedrohungswahrscheinlichkeit', 'Bedrohungsverteilung Dezember 2021 und November 2022', 'vergleich_bedrohung.png')

with open('p-Werte.txt', 'w') as file:
    file.write('Die Stichproben haben die Größen:\n')
    file.write('November 2021: ')
    file.write(str(tweet_count_2021))
    file.write('\n')
    file.write('Dezember 2022: ')
    file.write(str(tweet_count_2022))
    file.write('\n')
    file.write('Die p-Werte sind:\n')
    file.write('Genereller Hatespeech: ')
    file.write(str(general_hatespeech_p))
    file.write('\n')
    file.write('Toxizität: ')
    file.write(str(toxicity_p))
    file.write('\n')
    file.write('Schwere Toxizität: ')
    file.write(str(severe_toxicity_p))
    file.write('\n')
    file.write('Identitätsangriff: ')
    file.write(str(identity_attack_p))
    file.write('\n')
    file.write('Beleidigung: ')
    file.write(str(insult_p))
    file.write('\n')
    file.write('Obszönität: ')
    file.write(str(profanity_p))
    file.write('\n')
    file.write('Bedrohung: ')
    file.write(str(threat_p))
