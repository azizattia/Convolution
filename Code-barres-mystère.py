# mappage du code-barres
codabar_mapping = {
    '0000011': '0', '0000110': '1', '0001001': '2', '1100000': '3',
    '0010010': '4', '1000010': '5', '0100001': '6', '0100100': '7',
    '0110000': '8', '1001000': '9', '0001100': '-', '0001110': '$'
}

def process_simple_barcode(chemin_image):
    """ Mon code ici va parcourir une ligne horizontale du code-barres, puis vérifier si la barre rencontrée est fine ou large.
        En fonction de cela, il va sortir un 1 ou un 0. Lorsque nous obtenons 7 sorties, nous allons ensuite sauter un pixel,
        puis vérifier à quel numéro ou symbole correspond la séquence actuelle de 7 nombres."""
    
    # Charger l'image du code-barres
    image = imageio.imread(chemin_image)

    # Extraire une ligne du milieu de l'image
    ligne_mediane = image[image.shape[0] // 2, :]

    liste_binaire = []  # Pour stocker 7 valeurs binaires 0 pour les barres fines et 1 pour les barres larges
    ISBN = [] # Pour stocker le code ISBN a la fin
    i = 0

    while i < len(ligne_mediane):
        valeur_pixel = ligne_mediane[i]

        # Compter les pixels consécutifs de la même couleur (noir ou blanc)
        compte = 1
        for j in range(i+1, len(ligne_mediane)):
            if ligne_mediane[j] == valeur_pixel:
                compte += 1
            else:
                break

        # Classer en barre fine ou barre large
        if compte == 3:
            liste_binaire.append('1')  # barre large
        elif compte == 1:
            liste_binaire.append('0')  # barre fine

        # Une fois que nous avons 7 valeurs binaires les traiter et sauter 1 pixel
        if len(liste_binaire) == 7:
            chaine_binaire = ''.join(liste_binaire)

            # Mapper la chaîne binaire à un caractère Codabar
            if chaine_binaire in codabar_mapping:
                ISBN.append(codabar_mapping[chaine_binaire])


            liste_binaire = []  # Réinitialiser pour le groupe suivant
            i += compte + 1  # Sauter 1 pixel après traitement
        else:
            i += compte  # Passer au groupe de pixels suivant
            
    # afficher le code ISBN final        
    print("ISBN:", ''.join(ISBN))


chemin_image = 'tp1_ex2.png'
process_simple_barcode(chemin_image)
