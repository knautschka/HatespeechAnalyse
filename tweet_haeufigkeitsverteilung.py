import json
import matplotlib.pyplot as plt

tweets = []

with open('analyzed_tweets.json', 'r') as file:
    tweets = json.load(file)


# Hier werden die einzelnen Hatespeech-Werte der Tweets herausgefiltert und
# jeweils in einen Array gepackt
toxicity_values = []
severe_toxicity_values = []
identity_attack_values = []
insult_values = []
profanity_values = []
threat_values = []
general_hatespeech_percent = {
    '0-49 %': [],
    '50-100 %': []
}
for tweet in tweets:
    toxicity_score = tweet['attributeScores']['TOXICITY']['summaryScore']['value']
    severe_toxicity_score = tweet['attributeScores']['SEVERE_TOXICITY']['summaryScore']['value']
    identity_attack_score = tweet['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value']
    insult_score = tweet['attributeScores']['INSULT']['summaryScore']['value']
    profanity_score = tweet['attributeScores']['PROFANITY']['summaryScore']['value']
    threat_score = tweet['attributeScores']['THREAT']['summaryScore']['value']

    toxicity_percent = toxicity_score * 100
    severe_toxicity_percent = severe_toxicity_score * 100
    identity_attack_percent = identity_attack_score * 100
    insult_percent = insult_score * 100
    profanity_percent = profanity_score * 100
    threat_percent = threat_score * 100

    toxicity_values.append(toxicity_percent)
    severe_toxicity_values.append(severe_toxicity_percent)
    identity_attack_values.append(identity_attack_percent)
    insult_values.append(insult_percent)
    profanity_values.append(profanity_percent)
    threat_values.append(threat_percent)

    highest_value = max(toxicity_percent, severe_toxicity_percent, identity_attack_percent, insult_percent, profanity_percent, threat_percent)

    if highest_value >= 50:
        general_hatespeech_percent['50-100 %'].append(highest_value)
    else:
        general_hatespeech_percent['0-49 %'].append(highest_value)


# Ab hier werden alle Werte in die verschiedenen Gruppierungen eingeteilt
toxicity_groups = {
    '0-19 %': [],
    '20-49 %': [],
    '50-69 %': [],
    '70-89 %': [],
    '90-100 %': []
}

for value in toxicity_values:
    if value <= 19:
        toxicity_groups['0-19 %'].append(value)
    elif value <= 49:
        toxicity_groups['20-49 %'].append(value)
    elif value <= 69:
        toxicity_groups['50-69 %'].append(value)
    elif value <= 89:
        toxicity_groups['70-89 %'].append(value)
    else:
        toxicity_groups['90-100 %'].append(value)

severe_toxicity_groups = {
    '0-19 %': [],
    '20-49 %': [],
    '50-69 %': [],
    '70-89 %': [],
    '90-100 %': []
}

for value in severe_toxicity_values:
    if value <= 19:
        severe_toxicity_groups['0-19 %'].append(value)
    elif value <= 49:
        severe_toxicity_groups['20-49 %'].append(value)
    elif value <= 69:
        severe_toxicity_groups['50-69 %'].append(value)
    elif value <= 89:
        severe_toxicity_groups['70-89 %'].append(value)
    else:
        severe_toxicity_groups['90-100 %'].append(value)

identity_attack_groups = {
    '0-19 %': [],
    '20-49 %': [],
    '50-69 %': [],
    '70-89 %': [],
    '90-100 %': []
}

for value in identity_attack_values:
    if value <= 19:
        identity_attack_groups['0-19 %'].append(value)
    elif value <= 49:
        identity_attack_groups['20-49 %'].append(value)
    elif value <= 69:
        identity_attack_groups['50-69 %'].append(value)
    elif value <= 89:
        identity_attack_groups['70-89 %'].append(value)
    else:
        identity_attack_groups['90-100 %'].append(value)

insult_groups = {
    '0-19 %': [],
    '20-49 %': [],
    '50-69 %': [],
    '70-89 %': [],
    '90-100 %': []
}

for value in insult_values:
    if value <= 19:
        insult_groups['0-19 %'].append(value)
    elif value <= 49:
        insult_groups['20-49 %'].append(value)
    elif value <= 69:
        insult_groups['50-69 %'].append(value)
    elif value <= 89:
        insult_groups['70-89 %'].append(value)
    else:
        insult_groups['90-100 %'].append(value)

profanity_groups = {
    '0-19 %': [],
    '20-49 %': [],
    '50-69 %': [],
    '70-89 %': [],
    '90-100 %': []
}

for value in profanity_values:
    if value <= 19:
        profanity_groups['0-19 %'].append(value)
    elif value <= 49:
        profanity_groups['20-49 %'].append(value)
    elif value <= 69:
        profanity_groups['50-69 %'].append(value)
    elif value <= 89:
        profanity_groups['70-89 %'].append(value)
    else:
        profanity_groups['90-100 %'].append(value)

threat_groups = {
    '0-19 %': [],
    '20-49 %': [],
    '50-69 %': [],
    '70-89 %': [],
    '90-100 %': []
}

for value in threat_values:
    if value <= 19:
        threat_groups['0-19 %'].append(value)
    elif value <= 49:
        threat_groups['20-49 %'].append(value)
    elif value <= 69:
        threat_groups['50-69 %'].append(value)
    elif value <= 89:
        threat_groups['70-89 %'].append(value)
    else:
        threat_groups['90-100 %'].append(value)


# Ab hier startet das Ausgeben und Speichern der Diagramme

# Hier werden die einzelnen Häufigkeiten als Säulendiagramm ausgegeben

# Toxizitätsdiagramm
frequencies = {group: len(values) for group, values in toxicity_groups.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Toxizitätsgruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Toxizitätsgruppen')

plt.savefig('toxizitaet_diagramm.png')
plt.show()

# Schwere-Toxizitätsdiagramm
frequencies = {group: len(values) for group, values in severe_toxicity_groups.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Schwere-Toxizitätsgruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Schwere-Toxizitätsgruppen')

plt.savefig('schwere_toxizitaet_diagramm.png')
plt.show()

# Identitätsangriffsdiagramm
frequencies = {group: len(values) for group, values in identity_attack_groups.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Identitätsangriffsgruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Identitätsangriffsgruppen')

plt.savefig('identitaetsangriff_diagramm.png')
plt.show()

# Beleidigungsdiagramm
frequencies = {group: len(values) for group, values in insult_groups.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Beleidigungsgruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Beleidigungsgruppen')

plt.savefig('beleidigung_diagramm.png')
plt.show()

# Obszönitätsdiagramm
frequencies = {group: len(values) for group, values in profanity_groups.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Obszönitätsgruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Obszönitätsgruppen')

plt.savefig('obszoenitaet_diagramm.png')
plt.show()

# Bedrohungsdiagramm
frequencies = {group: len(values) for group, values in threat_groups.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Bedrohungsgruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Bedrohungsgruppen')

plt.savefig('bedrohung_diagramm.png')
plt.show()

# Vergleich der Anzahl von Tweets mit einem Wert von >= 50 % und < 50 %
frequencies = {group: len(values) for group, values in general_hatespeech_percent.items()}

labels = frequencies.keys()
values = frequencies.values()

plt.bar(labels, values)

plt.xlabel('Generelle Hatespeech-Gruppen')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Hatespeech-Gruppen')

plt.savefig('genereller_hatespeech_diagramm.png')
plt.show()

# Eine Textdatei wird ausgegeben, in der die absoluten und relativen Zahlen
# der Gruppierungen festgehalten werden.
with open('zusammenfassung.txt', 'w') as file:
    file.write('Generelle Hatespeech-Verteilung:\n')
    total_elements = sum(len(group) for group in general_hatespeech_percent.values())
    for group_name, elements in general_hatespeech_percent.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
    file.write('Verteilung der Toxizitätsgruppen:\n')
    total_elements = sum(len(group) for group in toxicity_groups.values())
    for group_name, elements in toxicity_groups.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
    file.write('Verteilung der Schwere-Toxizitätsgruppen:\n')
    total_elements = sum(len(group) for group in severe_toxicity_groups.values())
    for group_name, elements in severe_toxicity_groups.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
    file.write('Verteilung der Identitätsangriffsgruppen:\n')
    total_elements = sum(len(group) for group in identity_attack_groups.values())
    for group_name, elements in identity_attack_groups.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
    file.write('Verteilung der Beleidigungsgruppen:\n')
    total_elements = sum(len(group) for group in insult_groups.values())
    for group_name, elements in insult_groups.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
    file.write('Verteilung der Obszönitätsgruppen:\n')
    total_elements = sum(len(group) for group in profanity_groups.values())
    for group_name, elements in profanity_groups.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
    file.write('Verteilung der Bedrohungsgruppen:\n')
    total_elements = sum(len(group) for group in threat_groups.values())
    for group_name, elements in threat_groups.items():
        absolute_zahl = len(elements)
        percantage = (len(elements) / total_elements) * 100
        output_string = f"{absolute_zahl} ({percantage:.2f} %) der Tweets wurden mit {group_name} bewertet.\n"
        file.write(output_string)
    file.write('\n')
