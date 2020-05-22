# Modèle mathématiques :

Le système dynamique de l'étude de la répartition des richesses se fera en créant aléatoirement des couples au sein de la population, en leur donnant un nombre de descendant aléatoire qui auront chacun un salaire avec lui aussi un facteur aléatoire. Bien que chacun de ces évenements qui définiront l'hérédité sont aléatoire, il est bien évident qu'il necessite, pour obtenir une simulation plus réaliste, de faire varier ce paramètre aléatoire en fonction des charactéristiques des individus, afin que ceux-ci est plus ou moins de chance d'entrer en couple avec X, avoir Y enfants ou obtenir Z salaire, selon leur charactéristique. On définira les charactéristiques de chaque individu ainsi : Son Salaire et les charactéristiques de Abre Généalogique ( soit le salaire de ses ascendants ). Une seule contrainte s'impose : On souhaite qu'en Moyenne l'effectif de la population soit constant.

## Probabilité entre 2 individu d'être en couple selon leur salaire fonction paire :

Nécessite :

Fonction paire : f(x) = f(-x) étant donné que la fonction prend en paramètre les différences de salaires entre 2 individu et leur arbre genealogique respectif, on souhaite logiquement que la probabilité de A d'être en couple avec B soit la même que celle de B d'être en couple avec A, soit f(A-B) = f(B-A) soit f(x) = f(-x)
Lim f(x) x-> +-∞ = 0. On suppose que lorsque la différence de salaire tend à être grande, la probabilité d'être en couple diminue fortement.

Paramètre :

- FG : Facteur Généalogique / Génétique

- FS : Facteur Salariale ( 1 - FG )

- A : Affinité = Probabilité lorsque Différence Salariale et Généalogique = 0 (lorsque invidu sont identique salarialement et genealogiquement)

- T : Différence Salariale ou Généalogique à partir duquel la probabilité devient inférieure à 0.1*A (donc [-T,T] intervale de tolérance)

**f = A *( FS*exp(1.5*(DifférenceSalaire)²/T) + FG*exp(1.5*(DifférenceSalaireParents)²/T) )**

Remplie toute les conditions. ✅


## Probabilité pour un couple d'avoir 1,2 ou 3 enfants :

Necessite :

On souhaite que en Moyenne les couples aient 2 enfants, de telle manière que l'effectif de la population reste constant.
On appelle PX(Couple) la Probabilité du Couple d'avoir X enfants.
Pour chaque couple on a :

P1(Couple) + P2(Couple) + P3(Couple) = 1 (on élimine les cas 0 et plus de 3 enfants)

donc :

Σ ( P1(Couple) + P2(Couple) + P3(Couple) ) = N ( N est l'effectif des couples )

On suppose : 

P2(Couple) = constante = P2 (la probabilitée d'avoir 2 enfants est constante)

On souhaite : 

Σ ( P1(Couple)*1 + P2(Couple)*2 + P3(Couple)*3 ) / N = 2 ( Les couples ont 2 enfants en Moyenne )

On obtient ce système :

- Σ P1(Couple) + Σ P3(Couple) = N(1-P2)

- Σ P1(Couple) + 3*Σ P3(Couple) = 2N(1-P2)

duquel on déduit (Ligne 2 - 2*Ligne 1) :

- Σ P1(Couple) + Σ P3(Couple) = 0

- Σ P1(Couple) / N = Σ P3(Couple) / N

Si P2(Couple) est constante, il suffit que en moyenne, les couples aient autant de chance d'avoir 1 enfant que d'en avoir 3.

On cherche donc à construire les probabilités P1(Couple) et P3(Couple). On appelle S(Couple) le Salaire du couple.

On a Σ (S(Couple)) / N  = M (le salaire Moyen des Couples).

On a Σ (S(Couple)-M) = 0 = Σ (-S(Couple)+M)

On peut faire intervenir 2 constantes quelconques A et B et on à l'égalité :

( A*N + B*Σ (S(Couple)-M) ) / N = ( A*N + B*Σ (-S(Couple)+M) ) / N

( A*N + B*Σ (S(Couple)-M) ) / N = ( A*N + B*Σ (-S(Couple)+M) ) / N

puis

Σ (A + B*(S(Couple)-M)) / N = Σ (A + B*(-S(Couple)+M)) / N

Si on on appelle P1(Couple) = A + B*(S(Couple)-M) et P3(Couple) = A + B*(S(Couple)-M)

On a bien Σ P1(Couple) / N = Σ P3(Couple) / N

Or on obtient Σ P1(Couple) + Σ P3(Couple) = 2AN  = N(1-P2), on a donc necessairement A = (1-P2)/2.

On paramètrera B de manière à ce qu'on ait toujours P1(Couple) et P3(Couple) ∈ [0,1] donc |B| ⩽ (1-P2)/(2*Max(|S(Couple)-M|))
avec B > 0 on a :

P1(Couple) = (1-P2)/2 + (S(Couple)-M)(1-P2)/(2*Max(|S(Couple)-M|))

P2(Couple) = (1-P2)/2 + (-S(Couple)+M)(1-P2)/(2*Max(|S(Couple)-M|))

Car on souhaite que les couples étant plus riches tendent à avoir moins d'enfants et inversement.




## Fonction renvoyant le salaire de l'enfant selon un flottant aléatoire, le Salaire par Enfant du Couple et son Arbre Généalogique

[0,1] -> Salaire

Pour cela, on choisit un intervalle sur la répartition des salaires de la génération. Celui ci sera centré sur une portion dépendant du Salaire par Enfant des parents ( Facteur Social ), et sera d'une largeur égal à l'écart type de son arbre généalogique ( Facteur Génétique ). Une fois dans cet Intervalle on selectionne un salaire selon un nombre généré aléatoirement entre 0 et 1.
En ce qui concerne le pourcentage sur laquelle l'intervalle est centrée, on souhaite que celle-ci ne tende pas vers 0 de manière à modélisé un "accès minimal à une éducation". On souhaite également qu'elle tende vers 1 (intervalle centrée sur les plus riches) lorsque le salaire par enfant des parents est vraiment élevé.
On peut grossièrement approximer le centre de l'intervalle selon le salaire/enfant ainsi : (Arctan(Kx - A)/(τ/4) + 1 )*(1 - B)/2 + B
B représente les aides et l'éducation publique obligatoire, elle "assure" que l'intervalle ne pourra pas être centrée sur une portion inférieure à B (et que la pauvretée extrême ne sera donc pas fatale)
A représente le salaire à partir duquel une éducation plus qualitative (Privée et ou sur Paris/Grande Ville) est plus accessible.
On souhaite que à les enfants avec un salaire/enfant maximum se retrouve avec un intervale centrée sur 0.9 et donc on souhaite K(Salaire/Enfant MAX) - A = 2 soit K = (2 + A) / Salaire/Enfant MAX

Generation 0 :
