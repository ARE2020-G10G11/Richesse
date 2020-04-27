"""On identifie les Individus selon ces critères : Identifiant, 2 Parents, Génération, Salaire."""

#type Individu = tuple[int,tuple[int,int],int,float]



def MinEtPos(L) :
	"""list[Number] -> list[float]
	Renvoie le Minimum et sa position """
	for i in range(len(L)) :
		if len([k for k in L if k <L[i]]) == 0 :
			return [L[i],i]

def RangementCroissant(L) :
	"""list[float] -> list[float]
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
	Ls = []
	for i in L :
		_,_,_,_,S = i
		Ln.append(S)
	return Ls

def ListeSalaireCroissant(L) :
	"""list[Individu] -> list[float]
	Renvoie la liste croissante des salaires de la liste d'individu"""
	return RangementCroissant(ListeSalaire(L))

def ListeGeneration(L,n) :
	"""list[list[Individu]]*int -> list[Individu]
	Renvoie la liste des individu d'une Generation"""
	return L[n]

def ListeSalaireCroissantGeneration(L,n) :
	"""list[list[Individu]]*int -> list[float]
	Renvoie la liste croissante des salaires de la liste des individus d'une generation]"""
	return ListeSalaireCroissant(ListeGeneration(L,n))

def ArbreGenealogique(Ind,n,L) :
	"""Individu*int*list[list[Individu]] -> list[Individu]
	Renvoie la liste d'individu de l'arbre généalogique de Ind jusqu'à n générations en arrière"""
	Id,P,G,S = Ind
	P1,P2 = P
	if G == 0 :
		return []
	else :
		LP = []
		for Parent in L[G-1] :
			IdP,PP,_,_ = IndP
			if IdP == P1 or IdP == P2 :
				LP.append(IndP)
				
	return LP + ArbreGenealogique(LP[0],n-1,L) + ArbreGenealogique(LP[1],n,L)

	

def coeffgini(L) :

	

		
	
