import numpy as np
"""Ici on construit une matrice de notes, on suppose que les n premiers utilisateurs aiment les plats fats
et les autres(derniers) n'aiment pas les plats fats et que les m premiers plats sont fats et les autres non.

Une note negative ici c'est une note aléatoire entre 1 et 3 et une note positive c'est une note aléatoire entre 3 et 5"""

nbr_user = 15
nbr_item = 15
n = 3
m = 2

M11 = np.random.randint(3, size=(n, m)) + 1
M12 = np.random.randint(3, size=(n, nbr_item-m)) + 3
M21 = np.random.randint(3, size=(nbr_user-n, m)) + 3
M22 = np.random.randint(3, size=(nbr_user-n, nbr_item-m)) + 1
M = np.concatenate((M11, M12), axis=1)
M = np.concatenate((M, np.concatenate((M21, M22), axis=1)), axis=0)
print(M)