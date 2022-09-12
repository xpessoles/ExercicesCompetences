# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:42:21 2022

Réaliser la liste des exercices et remplir un tableau Excel. 
@author: xpess
"""

import os
folder_path = "C:\\GitHub\ExercicesCompetences"


def get_listes_exos(folder_path):
    """
    Réalise la liste des exos en retournant 
    rep, nom de fichier

    Parameters
    ----------
    folder_path : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    liste_exos = []
    for path, dirs, files in os.walk(folder_path):
        for filename in files : 
            if '.tex' in filename :
                ligne = path.split("\\")+[filename]
                if len(ligne)==7:
                    ligne = ligne[:-1]+[""]+[ligne[-1]]
                liste_exos.append(ligne)
    
    
    
    return liste_exos

def ecrire_csv(liste_exos,file_csv):   
    fid = open(file_csv,"w")
    fid.write(8*","+"\n")
    for ligne in liste_exos:
        ch =""     
        for mot in ligne :
            ch=ch+mot+','
        fid.write(ch[:-1]+"\n")
        
    fid.close()

def read_liste_dds(file):
    """
    Récupérer les exos d'un fichier dds

    Parameters
    ----------
    file : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    fid = open(file,"r")
    data = fid.readlines()
    fid.close()
    
    # Liste des compétences
    liste_comp = []
    for ligne in data :
        if "\\renewcommand{\\repExo}" in ligne :
            # On récupèr la fin de ligne
            l = ligne[32:]
            index = l.index("/")
            liste_comp.append(l[index+1:-2])
    # Liste des exos associés
    liste_exos = []
    for ligne in data :
        if "\\renewcommand{\\td}{" in ligne :
            # On récupèr la fin de ligne
            liste_exos.append(ligne[19:-2])
    
    
    return [[liste_comp[i],liste_exos[i]] for i in range(len(liste_comp))]

def association_exos_dds(liste_exos,liste_dds,num_dds):
    for dds in liste_dds : 
        for i in range(len(liste_exos)):
            #print(dds,liste_exos[i][-3])
            if dds[0] in liste_exos[i] :
                if dds[1] in liste_exos[i]:
                    liste_exos[i].append(num_dds)
                    
    return liste_exos


liste_exos = get_listes_exos(folder_path)

folder_path = "C:\\GitHub\ExercicesCompetences\Outils"
os.chdir(folder_path)


fichier_dds = "../../2022_2023_Enseignements/PSI_Etoile/DDS/DDS_01/DDS_01_liste.tex"

liste_dds = read_liste_dds(fichier_dds)

liste_exos = association_exos_dds(liste_exos, liste_dds,"DDS 1")
ecrire_csv(liste_exos,"liste_exos.csv")        

import pandas as pd

read_file = pd.read_csv('liste_exos.csv')
read_file.to_excel('liste_exos.xlsx', index = None, header=False)