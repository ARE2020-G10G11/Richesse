"""On identifie les Individus selon ces critères : Identifiant, 2 Parents, Génération, Salaire."""

#type Individu = tuple[int,tuple[int,int],int,float]

def MinEtPos(L) :
	"""list[Number] -> list[float]
	Renvoie le Minimum et sa position """
	for i in range(len(L)) :
		if len([k for k in L if k <L[i]]) == 0 :
			return [L[i],i]

def RangementCroissant(L) :
	"""list[int] -> list[int]
	Range la liste L dans l'odre croissant"""
	if len(L) == 0 :
		return []
	else :
		L1 = MinEtPos(L)
		return [L1[0]] + RangementCroissant(L[:L1[1]]+L[L1[1]+1:])

def Moyenne(L) :
	"""list[float] -> float
	Renvoie la Moyenne de la liste"""
	n = 0
	for i in L :
		n += i
	return n/len(L)

def MoyenneDistMoyenne(L) :
	"""list[float] -> float
	Renvoie la Moyenne des Distances à la Moyenne"""
	M = Moyenne(L)
	return(MoyenneDistMoyenne([abs(M-i) for i in L]))

def ListeSalaire(L) :
	"""list[Individu] -> list[float]
	Renvoie la liste des salaires de la liste d'individu"""
	Ln = []
	for i in L :
		_,_,_,_,k = i
		Ln.append(i)
	return Ln

def ListeSalaireCroissant(L) :
	"""List[Individu] -> List[int]
	Renvoie la liste croissante des salaires de la liste d'individu"""
	return RangementCroissant(ListeSalaire(L))

def coeffgini(L) :

	

		
	
