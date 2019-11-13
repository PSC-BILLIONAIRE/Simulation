import numpy as np

"""Ici on construit une matrice de notes, on suppose que les n premiers utilisateurs aiment les plats fats
et les autres(derniers) n'aiment pas les plats fats et que les m premiers plats sont fats et les autres non.

Une note negative ici c'est une note aléatoire entre 1 et 3 et une note positive c'est une note aléatoire entre 3 et 5"""


def substit_column(mat, i, j):
    """fonction pour substituer 2 colonnes i et j de la matrice M"""

    if i >= mat.shape[1] or j >= mat.shape[1]:
        raise ValueError("i and j have to be lower than the ssmatrix's number of column")
    else:
        t = mat[:, i].copy()
        mat[:, i] = mat[:, j]
        mat[:, j] = t
    return mat


def transform(mat):
    """Cette fonction va substituer des colonnes de la matrice M de facon aléatoire afin que la Matrice ait
    l'air moins strucuturée"""
    i = 0
    while i < (mat.shape[1]):
        a = np.random.randint(mat.shape[1])
        b = np.random.randint(mat.shape[1])
        mat = substit_column(mat, a, b)
        i = i + 1
    return mat


def RandomMatrix(nbr_user, nbr_item, n, m):
    if n > nbr_user or m > nbr_item:
        raise ValueError("n should be lower than nbr_user, same thing for m and nbr_item")

    M11 = np.random.randint(3, size=(n, m)) + 1
    M12 = np.random.randint(3, size=(n, nbr_item - m)) + 3
    M21 = np.random.randint(3, size=(nbr_user - n, m)) + 3
    M22 = np.random.randint(3, size=(nbr_user - n, nbr_item - m)) + 1
    M = np.concatenate((M11, M12), axis=1)
    M = np.concatenate((M, np.concatenate((M21, M22), axis=1)), axis=0)
    M = transform(M)
    return M


nbr_user = 5
nbr_item = 5
n = 3
m = 2
print(RandomMatrix(5,5,3,2))