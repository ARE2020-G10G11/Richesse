"""On identifie les Individus selon ces critères : Identifiant, 2 Parents, Génération, Salaire."""

#type Individu = tuple[int,tuple[int,int],int,float]

"""On appelera "ListeMonde" les Liste de Liste d'Individu, qui correspond à chacune des Generations. On appelera "Couple" les listes contenant 2 Individu formant un Couple"""

import sys
sys.setrecursionlimit(1000000)
import matplotlib.pyplot as plt
import numpy as np
import random

def MinEtPos(Liste) :
	"""list[float] -> list[float]
	Renvoie le Minimum de la liste et sa Position dans celle-ci """
	for Position in range(len(Liste)) :
		if len([Nombre for Nombre in Liste if Nombre<Liste[Position]]) == 0 :
			return [Liste[Position],Position]
		
def MaxEtPos(Liste) :
	"""list[float] -> list[float]
	Renvoie le Minimum de la liste et sa Position dans celle-ci """
	for Position in range(len(Liste)) :
		if len([Nombre for Nombre in Liste if Nombre>Liste[Position]]) == 0 :
			return [Liste[Position],Position]

def RangementCroissant(Liste) :
	"""list[float] -> list[float]
	Range la liste L dans l'odre croissant"""
	return np.sort(Liste)

def Moyenne(Liste) :
	"""list[float] -> float
	Renvoie la Moyenne de la liste"""
	if len(Liste) == 0 :
		return 0
	else :
		return np.mean(Liste)

def EcartType(Liste) :
	"""list[float] -> float
	Renvoie la Moyenne des Distances à la Moyenne"""
	if len(Liste) == 0 :
		return 0
	else :
		return np.std(Liste)


def SommeCumulée(Liste) :
	"""list[float] -> list[float]
	Renvoie la liste en somme cumulée de la liste L"""
	ListeCumulée = []
	Somme = 0
	for Nombre in Liste :
		Somme += Nombre
		ListeCumulée.append(Somme)
	return ListeCumulée
		
def CoefficientGini(Liste) :
	"""list[float] -> float
	Renvoie le coefficient de gini de la Liste"""
	Liste2 = SommeCumulée(RangementCroissant(Liste))
	Longueur = len(Liste2)
	Hauteur = Liste2[len(Liste2)-1]
	Aire = Liste2[0]/2
	for i in range(Longueur - 1) :
		Aire += (Liste2[i]+Liste2[i+1])/2	
	return 1 - 2*Aire/Hauteur*Longueur

def ListeSalaire(ListeIndividu) :
	"""list[Individu] -> list[float]
	Renvoie la liste des salaires de la liste d'individu"""
	ListeSalaire = []
	for Individu in ListeIndividu :
		_,_,_,Salaire = Individu
		ListeSalaire.append(Salaire)
	return ListeSalaire

def ArbreGenealogique(ListeMonde,Individu,NombreDeGeneration) :
	"""list[list[Individu]]*Individu*int -> list[Individu]
	Renvoie la liste d'individu de l'arbre généalogique de Ind jusqu'à n générations en arrière"""
	Identifiant,Parents,Generation,Salaire = Individu
	Parent1,Parent2 = Parents
	if Generation == 0 or NombreDeGeneration == 0 :
		return []
	else :
		ListeParents = []
		for Parent in ListeMonde[Generation-1] :
			IdentifiantParent,_,_,_ = Parent
			if IdentifiantParent == Parent1 or IdentifiantParent == Parent2 :
				ListeParents.append(Parent)
				
	return ListeParents + ArbreGenealogique(ListeMonde,ListeParents[0],NombreDeGeneration-1) + ArbreGenealogique(ListeMonde,ListeParents[1],NombreDeGeneration-1)

def ListeArbreGenealogiqueGeneration(ListeIndividu,ListeMonde,NombreDeGeneration) :
	"""list[list[Individu]]*Individu*int -> list[list[Individu]]
	Renvoie la liste des l'arbre généalogique des individus de la génération i jusqu'à n générations en arrière"""
	return [ArbreGenealogique(ListeMonde,Individu,NombreDeGeneration) for Individu in ListeIndividu]



def Probabilité(Individu1,Individu2,MSG1,ListeMonde,FacteurSalarial,Affinité,Tolérance,NombreDeGeneration) :
	"""Individu*Individu*float*float*float*list[list[Individu]]*int -> float"""
	_,_,_,S1 = Individu1
	_,_,_,S2 = Individu2
	DiffSG = MSG1 - Moyenne(ListeSalaire(ArbreGenealogique(ListeMonde,Individu2,NombreDeGeneration)))
	return  Affinité*(FacteurSalarial*np.exp(-1.5*((S1-S2)**2)/Tolérance)+(1-FacteurSalarial)*np.exp(-1.5*(DiffSG**2)/Tolérance))
			 
def ListeCouple(ListeIndividu,ListeMonde,FacteurSalariale,Affinité,Tolérance,NombreDeGeneration) :
	"""list[Individu]]*list[list[Individu]*float* -> list[list[Individu]]
	Renvoie la Liste des couples formées à partir de L"""
	ListeIndividu2 = ListeIndividu[::]
	ListeCouple = []
	while len(ListeIndividu2) > 1 :
		for Position in range(1,len(ListeIndividu2)) :
			MSG1 = Moyenne(ListeSalaire(ArbreGenealogique(ListeMonde,ListeIndividu2[0],NombreDeGeneration)))
			if random.random() <= Probabilité(ListeIndividu2[0],ListeIndividu2[Position],MSG1,ListeMonde,FacteurSalariale,Affinité,Tolérance,NombreDeGeneration) :
				ListeCouple.append([ListeIndividu2[0],ListeIndividu2[Position]])
				ListeIndividu2 = ListeIndividu2[2:Position] + ListeIndividu2[Position+1:]
				break
	return ListeCouple
		
def NombredEnfant(SalaireCouple,ProbabilitéDeuxEnfant,Moyenne,EcartMax) :
	"""list[list[Individu]]*float*float*float -> int
	Renvoie aléatoirement le nombre d'enfant qu'auront les 2 individus de L"""
	Random = random.random()
	if Random < ProbabilitéDeuxEnfant :
		return 2
	elif Random < ProbabilitéDeuxEnfant + (1-ProbabilitéDeuxEnfant)/2 + (SalaireCouple - Moyenne)*(1-ProbabilitéDeuxEnfant)/(2*EcartMax) :
		return 1
	else :
		return 3

def SalaireEnfant(SalaireParEnfant,Couple,ListeMonde,NombreDeGeneration,Population,SalaireMax,Effectif,Aide,Accessibilité) :
	Centre = (np.arctan(SalaireParEnfant*(2+Accessibilité)/SalaireMax - Accessibilité)/(np.pi/2) + 1)*(1-Aide)/2
	Random = random.random()
	EcartTypeV = EcartType(ListeSalaire(Couple + ArbreGenealogique(ListeMonde,Couple[0],NombreDeGeneration-1)+ArbreGenealogique(ListeMonde,Couple[1],NombreDeGeneration-1)))
	return Population[int(Centre*Effectif)] + (Random*2 - 1)*EcartTypeV
	
  
def Heredite(ListeIndividu,ListeMonde,FacteurSalariale,Affinité,Tolérance,NombreDeGeneration,ProbabilitéDeuxEnfant,Aide,Accessibilité):
  """list[Individu]*list[list[individu]]*float*float*float*int*float*float*float -> list[Individu]
  Renvoie la liste de la génération suivante à partir de la génération donnée"""
  NombredeNouveauIndividu = 1
  LNouvelleGeneration = []
  Population = RangementCroissant(ListeSalaire(ListeIndividu))
  Effectif = len(ListeIndividu)
  MoyenneV = Moyenne(ListeSalaire(ListeIndividu))
  EcartMax = MaxEtPos([abs(Salaire-MoyenneV) for Salaire in ListeSalaire(ListeIndividu)])[0]
  SalaireMax = MaxEtPos(ListeSalaire(ListeIndividu))[0]
  _,_,G,_ = ListeIndividu[0]
  for Couple in ListeCouple(ListeIndividu,ListeMonde,FacteurSalariale,Affinité,Tolérance,NombreDeGeneration) :
    Id1,_,_,S1 = Couple[0]
    Id2,_,_,S2 = Couple[1]
    NombredEnfantV = NombredEnfant((S1+S2)/2,ProbabilitéDeuxEnfant,MoyenneV,EcartMax)
    for i in range(NombredEnfantV) :
        LNouvelleGeneration.append((NombredeNouveauIndividu,(Id1,Id2),G+1,SalaireEnfant((S1+S2)/NombredEnfantV,Couple,ListeMonde,NombreDeGeneration,Population,SalaireMax,Effectif,Aide,Accessibilité)))
        NombredeNouveauIndividu += 1
  return LNouvelleGeneration

def Simulation(G0,Itération,FacteurSalariale,Affinité,Tolérance,NombreDeGeneration,ProbabilitéDeuxEnfant,Aide,Accessibilité) :
 """list[Individu]*int -> list[list[Individu]]"""
 ListeMonde = [G0]
 for I in range(Itération) :
   ListeMonde.append(Heredite(ListeMonde[I],ListeMonde,FacteurSalariale,Affinité,Tolérance,NombreDeGeneration,ProbabilitéDeuxEnfant,Aide,Accessibilité))
 return ListeMonde

def GraphPopulation(ListeMonde) :
	""" list[list[Individu]] -> None
	Affiche la population en salaire selon les différentes générations"""
	for ListeIndividu in ListeMonde :
		NombreIndividu = len(ListeIndividu)
		plt.plot([Fraction/NombreIndividu for Fraction in range(1,NombreIndividu)],[RangementCroissant(ListeSalaire(ListeIndividu))])
	plt.ylabel("Salaire")
	plt.legend(["G"+ str(i) for i in range(len(ListeMonde))])
	plt.show()
	return None

def GraphEffectif(ListeMonde) :
	""" list[list[Individu]] -> None
	Affiche la population en salaire différentes générations"""
	plt.plot([Generation for Generation in range(len(ListeMonde))],[len(ListeIndividu) for ListeIndividu in ListeMonde])
	plt.ylabel("Effectif")
	plt.xlabel("Generations")
	plt.show()
	return None

def GraphCoefficientGini(ListeMonde) :
       """ list[list[Individu]] -> None
       Affiche les coefficients de gini des différentes générations"""
       plt.plot([Generation for Generation in range(len(ListeMonde))],[CoefficientGini(ListeSalaire(ListeIndividu)) for ListeIndividu in ListeMonde])
       plt.xlabel("Generations")
       plt.ylabel("CoefficientGini")
       return None

def GraphEcartType(ListeMonde) :
       """ list[list[Individu]] -> None
       Affiche les EcartsType des différentes générations"""
       plt.plot([Generation for Generation in range(len(ListeMonde))],[EcartType(ListeSalaire(ListeIndividu)) for ListeIndividu in ListeMonde])
       plt.xlabel("Generations")
       plt.ylabel("EcartType")
       return None

def CreateurG0(Salaires,Pourcentages,OrdreDeGrandeur):
  """ list[float]*list[float]*Int -> list[Individu]
  Renvoie une génération 0 d'un certain ordre de grandeur à partir des Tableaux de Données entrés"""
  ListeGeneration0 = []
  NombredIndividu = 1
  for Position in range(len(Pourcentages)-1) :
    Section = int((Pourcentages[Position+1]-Pourcentages[Position])*10**(OrdreDeGrandeur))
    for I in range(Section):
      ListeGeneration0.append((NombredIndividu,(0,0),0,Salaires[Position] + I*(Salaires[Position+1]-Salaires[Position])/Section))
      NombredIndividu += 1
  return ListeGeneration0

SalairesG0 = [800,1034,1099,1133,1149,1169,1188,1207,1225,1242,1257,1272,1287,1302,1317,1332,1346,1360,1374,1387,1400,1412,1425,1439,1452,1466,1479,1493,1506,1520,1534,1548,1562,1576,1591,1606,1621,1637,1652,1668,1685,1701,1718,1735,1753,1771,1789,1807,1826,1845,1865,1885,1906,1927,1949,1972,1995,2018,2043,2068,2095,2122,2150,2179,2209,2240,2273,2307,2343,2379,2418,2460,2503,2549,2599,2652,2709,2768,2832,2899,2971,3048,3133,3226,3329,3445,3575,3724,3899,4104,4354,4668,5081,5665,6597,8629,10500]
PourcentagesG0 = [0] + [i/100 for i in range(5,101)]

i = CreateurG0(SalairesG0,PourcentagesG0,4)

X = Simulation(i,3,0.8,0.5,1000,2,1/3,1/3,2000)
GraphCoefficientGini(X)
GraphPopulation(X)
