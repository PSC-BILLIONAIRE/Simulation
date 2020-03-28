import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#Ce code est censé determiner l'influence qu'a le ranking sur la demande d'un plat
#je suppose ici qu'on a deja une fonction d'estimation de la demande qui ne prend pas en compte le ranking juste les notes et les prix


#Ici j'importe les données (qu'on est censé recueillir grace à l'app au debut)
donnees = pd.read_csv('données.csv', index_col=0)
donnees.head()


#créer un objet reg lin
modeleReg=LinearRegression()

#créer y et X
list_var=donnees.columns.drop("DemandeRanking") #il reste la demande sans rendre en compte le ranking et le ranking
y=donnees.DemandeRanking
X=donnees[list_var]

modeleReg.fit(X,y)
#pour preduire une demande il suffit de faire : modeleReg.predict(Xnew) ou Xnew contient la demande sans prendre en compte le ranking et un ranking