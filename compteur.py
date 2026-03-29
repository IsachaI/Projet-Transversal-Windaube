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

    return bien_places, mal_places