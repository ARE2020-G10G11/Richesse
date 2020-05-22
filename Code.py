"""On identifie les Individus selon ces critères : Identifiant, 2 Parents, Génération, Salaire."""

#type Individu = tuple[int,tuple[int,int],int,float]

"""On appelera "ListeMonde" les Liste de Liste d'Individu, qui correspond à chacune des Generations. On appelera "Couple" les listes contenant 2 Individu formant un Couple"""


%matplotlib inline
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
	if len(Liste) == 0 :
		return []
	else :
		MinEtPos = MinEtPos(Liste)
		return [MinEtPos[0]] + RangementCroissant(Liste[:MinEtPos[1]]+Liste[MinEtPos[1]+1:])

def Moyenne(Liste) :
	"""list[float] -> float
	Renvoie la Moyenne de la liste"""
	Somme = 0
	for Nombre in Liste :
		Somme += Nombre
	return Somme/len(Liste)

def MoyenneDistMoyenne(Liste) :
	"""list[float] -> float
	Renvoie la Moyenne des Distances à la Moyenne"""
	MoyenneListe = Moyenne(Liste)
	return Moyenne([abs(MoyenneListe-Nombre) for Nombre in Liste])

def EcartType(L)
	"""list[float] -> float
	Renvoie la Moyenne des Distances à la Moyenne"""
	MoyenneL = Moyenne(L)
	return Moyenne([(MoyenneL-i)**2 for i in L])**0.5
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
	for i in range(Longeur - 1) :
		B += (Liste2[i]+Liste2[i+1])/2	
	return 1 - 2*Aire/Hauteur*Longeur

def ListeSalaire(ListeIndividu) :
	"""list[Individu] -> list[float]
	Renvoie la liste des salaires de la liste d'individu"""
	ListeSalaire = []
	for Individu in ListeIndividu :
		_,_,_,_,Salaire = Individu
		ListeSalaire.append(Salaire)
	return ListeSalaire

def ArbreGenealogique(ListeMonde,Individiu,NombreDeGeneration) :
	"""list[list[Individu]]*Individu*int -> list[Individu]
	Renvoie la liste d'individu de l'arbre généalogique de Ind jusqu'à n générations en arrière"""
	Identifiant,Parents,Generation,Salaire = Individu
	Parent1,Parent2 = Parents
	if Generation == 0 :
		return []
	else :
		ListeParents = []
		for Parent in ListeMonde[Generation-1] :
			IdentifiantParent,_,_,_ = IndP
			if IdP == P1 or IdP == P2 :
				ListeParents.append(Parent)
				
	return ListeParents + ArbreGenealogique(ListeMonde,ListeParent[0],NombreDeGeneration-1) + ArbreGenealogique(ListeMonde,ListeParent[1],NombreDeGeneration-1)

def ListeArbreGenealogiqueGeneration(ListeIndividu,ListeMonde,NombreDeGeneration) :
	"""list[list[Individu]]*Individu*int -> list[list[Individu]]
	Renvoie la liste des l'arbre généalogique des individus de la génération i jusqu'à n générations en arrière"""
	return [ArbreGenealogique(ListeMonde,Individu,NombreDeGeneration) for Individu in ListeIndividu]



def Probabilité(Individu1,Individu2,MSG1,ListeMonde,FacteurSalarial,Affinité,Tolerance,NombreDeGeneration) :
	"""Individu*Individu*float*float*float*list[list[Individu]]*int -> float"""
	_,_,_,S1 = Individu1
	_,_,_,S2 = Individu2
	DiffSG = MSG1 - Moyenne(ListeSalaire(AbreGenealogique(ListeMonde,ListeIndividu2,NombreDeGeneration)))
	return  Affinité*(FacteurSalarial*exp(1.5*(S1-S2)²/Tolerance)+(1-FacteurSalarial)*exp(1.5*(DiffSG)²/Tolerance))
			 
def ListeCouple(ListeIndividu,ListeMonde,FacteurSalariale,Affinité,Tolerance,NombreDeGeneration) :
	"""list[Individu]]*list[list[Individu]*float* -> list[list[Individu]]
	Renvoie la Liste des couples formées à partir de L"""
	ListeIndividu2 = ListeIndividu[::]
	ListeCouple = []
	while len(ListeIndividu2) > 1 :
		for Position in range(1,len(ListeIndividu2)) :
			MSG1 = Moyenne(ListeSalaire(AbreGenealogique(ListeMonde,ListeIndividu2[0],NombreDeGeneration)))
			if random.random() <= Probabilité(ListeIndividu2[0],ListeIndividu2[Position],MSGInd1,ListeMonde,FacteurSalarial,Affinité,Tolerance,NombreDeGeneration) :
				ListeCouple.append([ListeIndividu2[0],ListeIndividu2[Position]])
				ListeIndividu2 = ListeIndividu2[2:Position] + ListeIndividu2[Position+1:]
				break
	return ListeCouple
		
def NombredEnfant(SalaireCouple,Probabilité2Enfant,Moyenne,EcartMax) :
	"""list[list[Individu]]*float*float*float -> int
	Renvoie aléatoirement le nombre d'enfant qu'auront les 2 individus de L"""
	Random = random.random()
	if Random < Probabilité2Enfant :
		return 2
	elif Random < Random Probabilité2Enfant + (1-Probabilité2Enfant)/2 + (SalaireCouple - Moyenne)*(1-Probabilité2Enfant)/(2*EcartMax) :
		return 1
	else :
		return 3

def SalaireEnfant(SalaireParEnfant,Couple,ListeMonde,NombreDeGeneration,Population,SalaireMax,Effectif,Aide,Accessibilité) :
	Centre = (arctan(SalaireParEnfant*(2+Accessibilité)/SalaireMax - Accessibilité)/(np.pi/2) + 1)*(1-Aide)/2
	Random = random.random()
	EcartType = EcartType(ListeSalaire(ArbreGenealogique(Couple[0],ListeMonde,NombreDeGeneration)+ArbreGenealogique(Couple[1],ListeMonde,NombreDeGeneration)))
	return Max(Population[Maxint(Centre*Effectif)] + (Random*2 - 1)*EcartType
	

def Heredite(ListeIndividu,ListeMonde,FacteurSalariale,Affinité,Tolerance,NombreDeGeneration,Probabilité2Enfant,Aide,Accessibilité) :
	"""list[Individu]*list[list[individu]]*float*float*float*int*float -> list[Individu]
	Renvoie la liste de la génération suivante à partir de la génération donnée"""
	LNouvelleGeneration = []
	Population = RangementCroissant(ListeSalaire(ListeIndividu))
	Effectif = len(ListeIndividu)
	Moyenne = Moyenne(ListeSalaire(ListeIndividu))
	EcartMax = MaxEtPos([abs(Salaire-Moyenne) for Salaire in ListeSalaire(ListeIndividu)])[0]
	SalaireMax = MaxEtPos(ListeSalaire(ListeIndividu))[0]
	_,_,G,_ = L[0]
	for Couple in ListeCouple(ListeIndividu,ListeMonde,FacteurSalariale,Affinité,Tolerance,NombreDeGeneration) :
		Id1,_,_,S1 = Couple[0]
		Id2,_,_,S2 = Couple[1]
		NombredEnfant = NombredEnfant((S1+S2)/2,Probabilité2Enfant,Moyenne,EcartMax)
		for i in range(NombredEnfant) :
			 LNouvelleGeneration.append(([len(LNouvelleGeneration),(Id1,Id2),G+1,SalaireEnfant((S1+S2)/NombredEnfant,Couple,ListeMonde,NombreDeGeneration,Population,SalaireMax,Effectif,Aide,Accessibilité)))
			 
			 
def Simulation(G0,Itération) :
	"""list[Individu]*int -> list[list[Individu]]"""
	ListeMonde = [G0]
	for i in range(Itération) :
		ListeMonde.append(Heredite(ListeMonde[len(ListeMonde)-1])
	return ListeMonde

def GraphPopulation(ListeMonde) :
	""" list[list[Individu]] -> None
	Affiche la population en salaire selon les différentes générations"""
	for ListeIndividu in ListeMonde :
		NombreIndividu = len(ListeIndividu)
		plt.plot([Fraction/NombreIndividu for Fraction in range(1,NombreIndividu)],[RangementCroissant(ListeSalaire(ListeIndividu))])
	plt.ylabel("Salaire")
	plt.legend(["G"+ str(i) for i in range(len(ListeMonde))]
	plt.show()
	return none

def GraphEffectif(ListeMonde) :
	""" list[list[Individu]] -> None
	Affiche la population en salaire différentes générations"""
	plt.plot([Generation for Generation in range(len(ListeMonde))],[len(ListeIndividu) for ListeIndividu in ListeMonde])
	plt.ylabel("Effectif")
	plt.xlabel("Generations")
	plt.show()
	return none

def GraphCoefficientGini(ListeMonde) :
       """ list[list[Individu]] -> None
       Affiche les coefficients de gini des différentes générations"""
       plt.plot([Generation for Generation in range(len(ListeMonde)],[CoefficientGini(ListeSalaire(ListeIndividu)) for ListeIndividu in ListeMonde])
       plt.xlabel("Generations")
       return none

def GraphEcartType(ListeMonde) :
       """ list[list[Individu]] -> None
       Affiche les EcartsType des différentes générations"""
       plt.plot([Generation for Generation in range(len(ListeMonde))],[EcartType(ListeSalaire(ListeIndividu)) for ListeIndividu in ListeMonde])
       plt.xlabel("Generations")
       return none

def CreateurG0(Salaires,Pourcentages,OrdreDeGrandeur)
       """ list[float]*list[float]*Int -> list[float]
       Renvoie une génération 0 d'un certain ordre de grandeur à partir des Tableaux de Données entrés"""
       ListeGeneration0 = []
       NombreDindividu = 1
       for Position in range(len(Pourcentages)-1) :
	       (Pourcentages[Position+1]-Pourcentages[Position])10**(OrdreDeGrandeur) = Section
	       for I in range(Section) :
			G0.append((NombreDindividu,(0,0),0,Salaires[Position] + I*(Salaires[Position+1]-Salaires[Position])/Section)
			NombreDindividu += 1
	return ListeGeneration0
					       
					       
	       
	       
	       
