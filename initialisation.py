# initialisation en dur
# /!\ NE PAS TOUCHER /!\
largeur_monde = "20"
hauteur_monde = "20"
temps_reproduction_poisson = "8"
temps_reproduction_requin = "12"
temps_energie_requin = "7"
chronon = "2"
nb_poissons_init = "10"
nb_requins_init = "10"

# Ouvrir un fichier en mode lecture
with open('monde.ini', 'r') as f:
    # Lire ligne par ligne
    line = f.readline()
    while line:
        # Traiter chaque ligne ici
        ligne = line.strip()
        if ligne.find('=') > 0:
            ligne = ligne.split('=')
            if ligne[0] == 'largeur_monde':
                largeur_monde = ligne[1]
            elif ligne[0] == 'hauteur_monde':
                hauteur_monde = ligne[1]
            elif ligne[0] == 'temps_reproduction_poisson':
                temps_reproduction_poisson = ligne[1]
            elif ligne[0] == 'temps_reproduction_requin':
                temps_reproduction_requin = ligne[1]
            elif ligne[0] == 'temps_energie_requin':
                temps_energie_requin = ligne[1]
            elif ligne[0] == 'chronon':
                chronon = ligne[1]
            elif ligne[0] == 'nb_poissons_init':
                nb_poissons_init = ligne[1]
            elif ligne[0] == 'nb_requins_init':
                nb_requins_init = ligne[1]
        line = f.readline()  # Lire la ligne suivante

# Fermer le fichier automatiquement à la fin du bloc 'with'