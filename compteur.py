def comparer(dicoMaster, dicoPlayer):
    bien_places = 0
    frequence_dicoMaster = {}
    frequence_dicoPlayer = {}

    for cle in dicoMaster:
        if dicoMaster[cle] == dicoPlayer[cle]:
            bien_places += 1
        else:
            frequence_dicoMaster[dicoMaster[cle]] = frequence_dicoMaster.get(dicoMaster[cle], 0) + 1
            frequence_dicoPlayer[dicoPlayer[cle]] = frequence_dicoPlayer.get(dicoPlayer[cle], 0) + 1
    mal_places = 0
    for couleur in frequence_dicoPlayer:
        if couleur in frequence_dicoMaster:
            mal_places += min(frequence_dicoMaster[couleur], frequence_dicoPlayer[couleur])

    print("Bien placés :", bien_places)
    print("Mal placés :", mal_places)
    return bien_places, mal_places

'''
TESTS UNITAIRES
dico1= {
    'rouge':(255, 0, 0),
    'bleu':(0, 0, 255),
    'orange':(255, 165, 0),
    'rose':(255, 138, 221),
    'bleu-clair':(100, 185, 249),
    'vert':(0, 128, 0),
    'jaune':(255, 255, 0),
    'blanc':(255, 255, 255)
}
#Rouge, rouge, blanc, bleu
dico1= {
    'led1': (255, 0, 0),
    'led2': (255, 0, 0),
    'led3': (255, 255, 255),
    'led4': (0, 0, 255)
}

#Rouge, rouge, jaune, bleu
dico2= {
    'led1': (255, 255, 255),
    'led2': (255, 255, 255),
    'led3': (255, 255, 255),
    'led4': (255, 255, 255)
}
comparer(dico1, dico2) #devrait retourner 2,1
'''



