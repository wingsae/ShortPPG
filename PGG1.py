# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:47:32 2023

@author: wingsae
"""

## Soll menschliches Verhalten darstellen 

import random

# Funktion zur Berechnung der Belohnung basierend auf den Beiträgen der Spieler
def calculate_reward(contributions):
    total_contribution = sum(contributions)
    individual_share = total_contribution / len(contributions)
    public_good = individual_share * 1.5  # Multiplikationsfaktor für den öffentlichen Nutzen
    return [public_good - contribution for contribution in contributions]

# Funktion zur Auswahl der Aktion basierend auf dem menschlichen Verhalten
def choose_action(contributions, fsm_threshold):
    total_contribution = sum(contributions)
    average_contribution = total_contribution / len(contributions)

    if average_contribution >= fsm_threshold:
        return random.randint(0, 100)  # Zufällige Aktion, wenn der Durchschnittsbeitrag hoch genug ist
    else:
        return 0  # Kein Beitrag, wenn der Durchschnittsbeitrag zu niedrig ist

# Hauptprogramm
def main():
    num_players = 4
    contributions = []
    fsm_threshold = 50  # Schwellenwert 

    for _ in range(num_players):
        contribution = random.randint(0, 100)  # Zufälliger Beitrag für jeden Spieler
        contributions.append(contribution)

    print("Aktuelle Beiträge:", contributions)
    best_action = choose_action(contributions, fsm_threshold)
    print("Beste Aktion:", best_action)

    rewards = calculate_reward(contributions)
    print("Belohnungen:", rewards)

if __name__ == "__main__":
    main()
