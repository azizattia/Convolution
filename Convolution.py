# Votre solution ici. Ajoutez des cellules de code ou de type Markdown (pour expliquer votre solution).

def convolution(image:np.ndarray, noyau:np.ndarray, padding:str='zero') -> np.ndarray:
    """Convolution d'une image en niveaux de gris avec un noyau de convolution.
    Paramètres
    ----------
    image : ndarray
        Image en niveaux de gris de taille (H, W)
    noyau : ndarray
        Noyau de convolution de taille (h, w)
    padding : str, optionnel
        Type de remplissage pour les conditions de frontière. 
        'zero' pour un remplissage de zéro, 'mirror' pour un remplissage miroir.
    Retour
    -------
    ndarray
        Image convoluée de taille (H, W)
    """
    # Obtenir les dimensions de l'image et du noyau
    H, W = image.shape
    h, w = noyau.shape
    
    # Tailles du padding
    pad_h = h // 2
    pad_w = w // 2
    
    # Appliquer le padding à l'image
    if padding == 'zero':
        # ajouter des zero autour de l'image
        padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    elif padding == 'mirror':
        # Reflète l'image autour de ses bordures
        padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='reflect')
    
    # Initialiser le tableau de sortie avec des zeros
    sortie = np.zeros((H, W))
    
    # Retourner le noyau pour la convolution
    noyau_inverse = np.flipud(np.fliplr(noyau))
    
    # Effectuer la convolution
    for i in range(H):
        for j in range(W):
            # Extraire la région d'intérêt de l'image paddée
            region = padded_image[i:i+h, j:j+w]
            # Appliquer le noyau
            sortie[i, j] = np.sum(region * noyau_inverse)
    
    # Normaliser et limiter les valeurs de sortie pour correspondre au type de l'image d'entrée
    sortie = np.clip(sortie, 0, 255).astype(np.uint8)
    
    return sortie

# ici je vais juste ajouter le code pour faire l'affichage et l'enregistrement des images avec les filtres
# Charger l'image
image = imageio.imread('tp1_ex1.tif')

# Définir les noyaux
# Filtre moyenneur 5x5
moyenneur_kernel = np.ones((5, 5)) / 25

# Filtre gaussien 5x5
gaussian_kernel = np.array([[1, 4, 7, 4, 1],
                            [4, 16, 26, 16, 4],
                            [7, 26, 41, 26, 7],
                            [4, 16, 26, 16, 4],
                            [1, 4, 7, 4, 1]]) / 273

# Filtre Sobel horizontal
sobel_kernel = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

# Appliquer la convolution avec différents noyaux
convoluted_moyenneur = convolution(image, moyenneur_kernel, padding='zero')
convoluted_gaussian = convolution(image, gaussian_kernel, padding='zero')
convoluted_sobel = convolution(image, sobel_kernel, padding='zero')

# Enregistrer les images filtrées en format PNG (en s'assurant qu'elles sont en uint8)
imageio.imwrite('convoluted_moyenneur.png', convoluted_moyenneur.astype(np.uint8))
imageio.imwrite('convoluted_gaussian.png', convoluted_gaussian.astype(np.uint8))
imageio.imwrite('convoluted_sobel.png', convoluted_sobel.astype(np.uint8))

# Tracer l'image originale et les images convoluées
plt.figure(figsize=(12, 8))

# Image originale
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Image originale')

# Résultat du filtre moyenneur
plt.subplot(2, 2, 2)
plt.imshow(convoluted_moyenneur, cmap='gray')
plt.title('Filtre moyenneur')

# Résultat du filtre gaussien
plt.subplot(2, 2, 3)
plt.imshow(convoluted_gaussian, cmap='gray')
plt.title('Filtre Gaussien')

# Résultat du filtre Sobel horizontal
plt.subplot(2, 2, 4)
plt.imshow(convoluted_sobel, cmap='gray')
plt.title('Filtre Sobel Horizontal')

plt.show()
