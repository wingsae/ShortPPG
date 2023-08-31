# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:42:56 2023

@author: wingsae
"""

import random
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Belohnung basierend auf den Beiträgen der Spieler
def calculate_reward(contributions):
    total_contribution = sum(contributions)
    individual_share = total_contribution / len(contributions) #Eigener Anteil
    public_good = individual_share * 1.5  # Multiplikationsfaktor für den öffentlichen Nutzen
    return [public_good - contribution for contribution in contributions]

# Funktion zur Auswahl der besten Aktion basierend auf FSM
def choose_action(contributions):
    possible_contributions = range(0, 101)  # Mögliche Beiträge von 0 bis 100
    best_action = None
    best_reward = float('-inf')
    rewards = []

    for contribution in possible_contributions:
        current_contributions = contributions + [contribution]
        reward = sum(calculate_reward(current_contributions))
        rewards.append(reward)
        if reward > best_reward:
            best_reward = reward
            best_action = contribution

    # Balkendiagramm der Belohnungen anzeigen
    plt.bar(possible_contributions, rewards)
    plt.xlabel('Aktion')
    plt.ylabel('Belohnung')
    plt.title('Belohnungen für verschiedene Aktionen')
    plt.show()

    return best_action

# Hauptprogramm
def main():
    num_players = 4
    contributions = []

    for _ in range(num_players):
        contribution = random.randint(0, 100)  # Zufälliger Beitrag für jeden Spieler
        contributions.append(contribution)

    print("Aktuelle Beiträge:", contributions)
    best_action = choose_action(contributions)
    print("Beste Aktion:", best_action)

if __name__ == "__main__":
    main()
