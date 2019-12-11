#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:52:27 2019

@author: zoureni
"""

print("Bienvenue au jeu du Mashup")

# Demander au joueur d'entrer les données

nom_complet1 = input("entrer un premier nom et prenom :  ")
nom_complet2 = input("entrer un deuxième nom et prenom :  ")

# Utiliser "l'espace" pour séparer le nom et le prénom
l_espace = nom_complet1.find(" ")
nom1 = nom_complet1[0:l_espace]
prenom1 = nom_complet1[l_espace + 1 : len(nom_complet1)]

l_espace = nom_complet2.find(" ")
nom2 = nom_complet2[0:l_espace]
prenom2 = nom_complet2[l_espace + 1 : len(nom_complet2)]


# Definir la taille des noms et prenoms
taille_nom1 = len(nom1)
taille_nom2 = len(nom2)
taille_prenom1 = len(prenom1)
taille_prenom2 = len(prenom2)

# Diviser les noms et prenoms en 2
index_nom1 = int(taille_nom1 / 2)
index_nom2 = int(taille_nom2 / 2)
index_prenom1 = int(taille_prenom1 / 2)
index_prenom2 = int(taille_prenom2 / 2)

# Definir les moitiés des noms 
demi1_nom1 = nom1[0:index_nom1]
demi2_nom1 = nom1[index_nom1:taille_nom1]
demi1_nom2 = nom2[0:index_nom2]
demi2_nom2 = nom2[index_nom1:taille_nom2]

# Définir les moités des prénoms
demi1_prenom1 = prenom1[0:index_prenom1]
demi2_prenom1 = prenom1[index_prenom1:taille_prenom1]
demi1_prenom2 = prenom2[0:index_prenom2]
demi2_prenom2 = prenom2[index_prenom2:taille_prenom2]

# Associer par 2 les moités de nom
nouveau_nom1 = demi1_nom1 + demi2_nom2
nouveau_nom2 = demi2_nom1 + demi1_nom2
nouveau_nom3 = demi2_nom2 + demi1_nom1
nouveau_nom4 = demi1_nom2 + demi2_nom1

# Associer par 2 les moitiés de prénom
nouveau_prenom1 = demi1_prenom1 + demi2_prenom2
nouveau_prenom2 = demi2_prenom1 + demi1_prenom2
nouveau_prenom3 = demi2_prenom2 + demi1_prenom1
nouveau_prenom4 = demi1_prenom2 + demi2_prenom1

# Imprimer les nouveaux noms
print(("Possibilité N1: ") , (nouveau_nom1), (nouveau_prenom1))
print(("Possibilité N2: ") , (nouveau_nom3), (nouveau_prenom3))
print("Faites votre choix ")
print("MERCI")

