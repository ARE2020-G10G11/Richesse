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
	return Moyenne([abs(M-i) for i in L])

def EcartType(L)
	"""list[float] -> float
	Renvoie la Moyenne des Distances à la Moyenne"""
	M = Moyenne(L)
	return Moyenne([(M-i)**2 for i in L])**0.5

def ListeSalaire(L) :
	"""list[Individu] -> list[float]
	Renvoie la liste des salaires de la liste d'individu"""
	Ls = []
	for i in L :
		_,_,_,_,S = i
		Ln.append(S)
	return Ls

def ListeGeneration(L,n) :
	"""list[list[Individu]]*int -> list[Individu]
	Renvoie la liste des individu d'une Generation"""
	return L[n]

def ArbreGenealogiqueNGenerations(L,Ind,n) :
	"""list[list[Individu]]*Individu*int -> list[Individu]
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

def ListeArbreGenealogiqueNGenerationièmeGeneration(L,n,i) :
	"""list[list[Individu]]*Individu*int -> list[list[Individu]]
	Renvoie la liste de liste d'individu de l'arbre généalogique des individus de la génération i jusqu'à n générations en arrière"""
	return [ArbreGenealogiqueNGenerations(L,Ind,n) for Ind in L[i]]

def SommeCummulé(L) :
	"""list[float] -> list[float]
	Renvoie la liste en cummulé de la liste L"""
	LC = []
	S = 0
	for i in L :
		S += i
		LC.append(S)
	return LC
		
def CoeffGini(L) :
	"""list[float] -> float
	Renvoie le coefficient de gini de la liste"""
	N = len(L)
	T = L[len(L)-1]
	S = 0
	B = L[0]/2
	for i in range(len(L)-1) :
		B += (L[i]+L[i+1])/2	
	return 1 - 2*B/T*N


def CoeffGiniSalaireListeIndividu(L) :
	"""list[Individu] -> float
	Renvoie le coefficient de gini des salaires de la liste d'Individu"""
	return CoeffGini(SommeCummulé(RangementCroissant(ListeSalaire(L))))

def EcartTypeSalaireListeIndividu(L) :
	"""list[Individu] -> float
	Renvoie l'écart type des salaires de la liste d'Individu"""
	return 



	
		
	
	

	

		
	
