# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 16:12:33 2023

@author: wingsae
"""

# Verwendet QLearning 

import random
import numpy as np

class Player:
    def __init__(self, budget):
        self.budget = budget
        self.q_table = np.zeros((budget+1, budget+1))

    def make_contribution(self, other_players):
        state = self.budget
        action = self.choose_action(state)
        contribution = min(action, self.budget)
        self.budget -= contribution
        return contribution

    def choose_action(self, state):
        if random.uniform(0, 1) < epsilon:
            # Zufällige Aktion wählen
            return random.randint(0, state)
        else:
            # Beste Aktion aus Q-Tabelle wählen
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        # Q-Wert aktualisieren
        self.q_table[state, action] += learning_rate * (reward + discount_factor * np.max(self.q_table[next_state]) - self.q_table[state, action])

def play_game(players, rounds):
    for round in range(rounds):
        contributions = []
        total_contribution = 0

        # Jeder Spieler trifft eine Entscheidung und trägt zum Gesamtbetrag bei
        for player in players:
            contribution = player.make_contribution(players)
            contributions.append(contribution)
            total_contribution += contribution

        # Der Gesamtbetrag wird verdoppelt und gleichmäßig auf alle Spieler aufgeteilt
        total_contribution *= 2
        payoff = total_contribution / len(players)

        # Spieler erhalten ihren Gewinn basierend auf ihrer Einzahlung
        for i, player in enumerate(players):
            player.budget += payoff

        # Ergebnisse anzeigen
        print(f"Runde {round+1}:")
        for i, player in enumerate(players):
            print(f"Spieler {i+1}: Budget = {player.budget}")

        # Q-Tabelle aktualisieren
        for i, player in enumerate(players):
            state = player.budget + contributions[i]
            action = contributions[i]
            reward = payoff - contributions[i]
            next_state = player.budget
            player.update_q_table(state, action, reward, next_state)

# Hyperparameter
epsilon = 0.1  # Epsilon-Greedy-Parameter
learning_rate = 0.1  # Lernrate
discount_factor = 0.9  # Diskontierungsfaktor

# Spieler erstellen
player1 = Player(10)
player2 = Player(10)
player3 = Player(10)
player4 = Player(10)

# Spiel starten
players = [player1, player2, player3, player4]
play_game(players, 5)  # Anzahl der Runden angeben

