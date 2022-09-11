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
                liste_exos.append([path,filename])
    return liste_exos

def ecrire_csv(liste_dir,file_csv):
    fid = open(file_csv,"w")
    for ligne in liste_dir:
        ch = ""
        path = ligne[0][31:] # Suppression du début du chemein
        fichier = ligne[1]
        
        pi = 0
        
        while path.count("\\")>0 :
            ch = ch+path[0:path.index("\\")]+";"
            path = path[path.index("\\")+1:]
            pi = pi+1
        if pi ==2 : 
            ch = ch+";"
        ch=ch+fichier+"\n "

        fid.write(ch)
        
    fid.close()
    
liste_exos = get_listes_exos(folder_path)

folder_path = "C:\\GitHub\ExercicesCompetences\Outils"
os.chdir(folder_path)

ecrire_csv(liste_exos,"liste_exos.csv")        
