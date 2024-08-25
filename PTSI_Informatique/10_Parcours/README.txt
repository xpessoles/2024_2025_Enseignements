Bonjour vous procédez comment pour détecter un cycle dans un graphe à partir des parcours en profondeur/largeur? En regardant si un des voisins du sommet courant dans le parcours a déjà été marqué? 


Pierre Le Scornet (Vannes)
2:37 PM
En sachant s'il est encore ouvert


Antoine Domenech
2:37 PM
DFS récursif. Si un sommet voit un voisin ouvert non encore ferme, il y a un cycle (et on peut même le récupérer via l'arbre induit).

Si le graphe est non orienté on ajoute la condition que le voisin en question n'est pas le sommet doù l'on vient. 


Nathaniel Carré
2:39 PM
c'est pas le plus efficace, mais généralement, ce que je choisis c'est :

dans un graphe non orienté, vérifier si 
∣
 
∣
−
 
<
∣
 
∣
∣S∣−m<∣A∣, où 
 
m est le nombre de composantes connexes ;
dans un graphe orienté, vérifier s'il existe une arête 
(
 
,
 
)
(s,t) telle que 
 
 
 
 
(
 
)
<
 
 
 
 
(
 
)
post(s)<post(t), où 
 
 
 
 
post donne le numéro dans l'ordre d'un parcours en profondeur postfixe

arnaud
2:40 PM
et si on ne s'adresse pas à des MP2I ?  :sweat_smile: 

un sommet ouvert c'est bien un sommet marqué qui possède un voisin non marqué ?


np
2:47 PM

Il faut par contre bien faire attention dans un graphe non orienté à traiter différemment le sommet d'où tu viens. Et le cas non orienté pas besoin de distinguer ouvert et fermé. 


Nathaniel Carré
2:48 PM

j'ai pas testé, mais je pense que quelque chose comme ça doit marcher :

def sans_cycle_orienté(G):
    n = len(G)
    marque = [0] * n
    def DFS(s):
        if marque[s] == 0:
            marque[s] = 1
            for t in G[s]:
                if not DFS(t):
                    return False
            marque[s] = 2
        return marque[s] == 2
    for s in range(n):
        if marque[s] == 0 and not DFS(s):
            return False
    return True
ici, marque[s] vaut 0 si non ouvert, 1 si ouvert non fermé et 2 si fermé


np
2:52 PM

Pour un graphe orienté uniquement ? 


arnaud
2:56 PM

Ce que j'ai dit au dessus ça ne fonctionne que pour un graphe non orienté ?

Pour pouvoir dire que deux chemins différents qui mènent à un même sommet donnent l'existence d'un cycle.


np
2:58 PM

Qu'est-ce que tu appelles "marqué" ?

2:58 PM
Tel quel, pour moi, ce que tu as dit ci-dessus ne fonctionne dans aucun des deux cas.


arnaud
2:59 PM

tu marques un sommet lorsqu'il est visité par le parcours. Je parle d'un parcours en profondeur. 


np
2:59 PM

Pour le cas orienté il faut retomber sur un somment encore dans la pile de récursion (ouvert mais non fermé, ce que j'appelle actif). Pour le cas non orienté, il faut distinguer le parent du sommet exploré, qui lorsqu'il existe est toujours un voisin marqué. 


np
2:59 PM

À quel moment ?

3:00 PM
Il y a plusieurs manières de faire et il faut être relativement précis pour ce genre de problématiques.


arnaud
3:00 PM
La première fois que tu le visites


np
3:00 PM
Bon, alors qu'est-ce que tu appelles "visiter" :slightly_smiling_face:.


arnaud
3:00 PM
quand tu le dépiles


np
3:00 PM
Je suis peut-être pénible mais tout ceci est assez délicat en fait.


arnaud
3:03 PM

lorsqu'un sommet est dépilé: s'il n'est pas marqué on le marque et on empile tous ses voisins, ce que j'appelle "visiter" (sinon on ne fait rien et on dépile un autre sommet). 


np
3:04 PM
Tu es d'accord que pour un graphe non orienté, à part si c'est le tout premier sommet à partir duquel tu lances le parcours, il y aura toujours un sommet marqué dans ses voisins : celui à partir duquel il a été découvert ? 


arnaud
3:05 PM

Oui son prédécesseur?


np
3:06 PM
Donc il te faut un moyen de tester ce cas.


np
3:08 PM

Et pour un graphe orienté, tu peux très bien retomber sur un sommet déjà marqué sans cycles. Considère par exemple le graphe 
1
→
0
1→0, 
2
→
0
2→0 dans lequel ton parcours commence par le sommet 
0
0 puis le sommet 
1
1 puis le sommet 
2
2. 


arnaud
3:09 PM
oui pour les graphes orientés mon raisonnement est faux. Mais je ne comprends pas pourquoi il est faux pour les graphes non orientés?


np
3:10 PM
Si tu prends le graphe 
0
−
1
0−1 et que tu fais un parcours à partir de 
0
0, tu l'empiles, tu le dépiles, le marques et ajoutes 
1
1 dans la pile. Quand tu traites 
1
1, tu le dépile, tu le marques et tu trouves le voisin 
0
0 marqué donc tu indiques qu'il y a un cycle, alors qu'il n'y en a pas. 


arnaud
3:11 PM
Ah oui tu es pénible  :sweat_smile: 


np
3:15 PM

Le code de @Nathaniel Carré s'adapte simplement au cas non orienté :

def sans_cycle_orienté(G):
    n = len(G)
    marque = [0] * n
    def DFS(s, p):
        if marque[s] == 0:
            marque[s] = 1
            for t in G[s]:
                if not DFS(t, s):
                    return False
            marque[s] = 2
        return s == p || marque[s] == 2
    for s in range(n):
        if marque[s] == 0 and not DFS(s, -1):
            return False
    return True

Florian Hatat
3:15 PM
En oraux blancs, j'ai planté un nombre incroyable d'élèves avec ça ("il existe une suite d'arêtes d'un sommet vers lui même donc c'est un cycle").


arnaud
3:19 PM

Bon mais si la suite a au moins deux arêtes consécutives distinctes c'est ok non ? 


np
3:21 PM
Si c'est universel oui si c'est existentiel non.


arnaud
3:21 PM

en fait j'aurais bien aimé ne pas utiliser une fonction récursive


np
3:21 PM
Alors tu peux empiler les couples (sommet, parent).

3:22 PM
Ou avoir un tableau parent à côté.

3:22 PM
Mais pourquoi ne pas vouloir le faire en récursif ? Le parcours en profondeur est fondamentalement récursif.


arnaud
3:25 PM

parce qu'avec la récursivité on ne maîtrise pas bien le nombre de sous-appels récursifs. 

Mais je le garde sous le coude.

Merci des explications je n'avais pas bien saisi les difficultés de la recherche de cycle.


Nathaniel Carré
3:43 PM

je ne vois pas en quoi on maîtrise mieux le nombre de passages dans une boucle while


np
3:45 PM
Je pense qu'il fait référence au problème de débordement de la pile d'appels récursifs.


Axel Rogue
4:19 PM
Salut,
J'ai une question à propos de l'accueil des nouveaux élèves de sup (PTSI dans mon cas, mais ça ne change pas grande chose).

Est-ce que certains d'entre vous donnent à faire une sorte de cahier de vacances pour ceux qui veulent se préparer un peu en Juillet-Aout ?
Soit sous forme d'un cahier "classique", soit sous forme d'un parcours à faire en ligne (je pense par exemple à https://www.france-ioi.org/algo/chapters.php).

Dans ma prépa jusqu'ici, on avait ajouté une partie "Informatique" au cahier de calcul qu'on envoie aux futurs élèves, mais je ne pense pas que ce soit un format très engageant et que les jeunes le fasse (alors que plusieurs m'ont dit que la partie calcul leur avait servi).
Le but est de diminuer, au moins un peu, la proportions d'élèves qui ne savent rien de rien sur python au début de l'année.


jbb 🐈‍⬛
4:50 PM
Pour les MP2I on leur conseille de faire un peu de france-ioi pendant l'été. Les premiers niveaux ne sont pas très intéressants (et ne peuvent être sautés), mais c'est mieux que rien. 


matthieu_solnon
5:02 PM

Avec les collègues de sup, on s'était mis d'accord pour conseiller aux futurs sup de faire les 2-3 premiers niveaux de France IOI. 
Je n'ai pas suivi le dossier, je ne sais pas si cela a été suivi d'effets. 


jbb 🐈‍⬛
5:06 PM
Chez nous c'est dans le message envoyé par Parcoursup quand ils acceptent définitivement, avec « lire les livres au programme de Français ».

Système
11:20 PM
@Asli Grimaud a rejoint le canal.
Aujourd'hui

Pierre Karpman
10:51 AM
Hello,
Puisqu'on parle de DFS, j'ai relu les messages du 15 juin sur l'implémentation itérative avec pile et les défauts / dangers associés.
Pour ce qui est de la consommation mémoire supplémentaire de dfs2, il y a une solution simple qui consiste à utiliser une structure un peu plus riche qu'une pile, permettant la suppression (en ≈ O(1)) d'un élément connu : avant d'empiler un sommet, il suffit de vérifier s'il est déjà présent plus bas dans la pile, et si oui on le supprime (car il aura déjà été visité quand on le dépilera). Ça s'implémenterait bien avec une liste doublement chaînée, mais en python on n'a pas vraiment ça (en tout cas, les deques ne permettent pas la suppression rapide hors tête/queue). Par contre, les dictionnaires implémentent une structure de pile, grâce à popitem qui est garantie (depuis la version 3.7) de renvoyer le dernier élément inséré.

Bref, du coup ça donne ça (en modifiant a minima le dfs2 de https://11011110.github.io/blog/2013/12/17/stack-based-graph-traversal.html  déjà cité) :

def dfs2lite(G, s):
    visited = set()
    rastack = {s: True}
    while rastack:
        v, _ = rastack.popitem()
        if v not in visited:
            visited.add(v)
            for w in G[v]:
                if w not in visited:
                    if w in rastack:
                        del rastack[w]
                    rastack[w] = True
    return visited
Les dictionnaires étant au programme (et le choix «éclairé» entre liste et dictionnaire aussi  :sweat_smile: ), ça me semble pas complètement déconnant de traiter ça en cours, non ?


g_dewaele
11:17 AM
Je ne peux personnellement m'empêcher de trouver ça un peu compliqué pour des élèves, d'autant que ça suppose que ce soit une version récente de Python, pour pouvoir avoir la condition sur l'ordre des clés afin de garantir que le popitem donne la bonne clé, et il faut encore expliquer pourquoi on supprime une clé pour la remettre toujours sur ce même principe. Et il me semble que ça déborde pas mal du programme...


Pierre Karpman
11:35 AM
Oui, ça ferait un peu des choses à expliquer (pour la suppression/réinsertion, la doc est au moins bien claire sur le sujet : “Dictionaries preserve insertion order. Note that updating a key does not affect the order. Keys added after deletion are inserted at the end.”, donc si on donne l'extrait correspondant ce n'est pas bien méchant), et je n'ai aucune expérience d'enseignement en prépa, donc je te crois si tu penses que c'est un peu compliqué. Mais par contre je ne vois pas pourquoi tu trouves que ça déborde pas mal du programme (vraie question) ?


g_dewaele
1:14 PM
Je ne suis pas convaincu que savoir que les dictionnaires préservent l'ordre des clés (officiellement seulement depuis Python 3.7, même si c'est apparu en 3.6) soit un attendu du programme. popitem en particulier (qui permet d'utiliser un dictionnaire comme une pile) me semble un peu loin. En fait, si un élève écrit quelque chose du genre en concours, je ne suis pas convaincu que ça se passerait bien, je ne suis pas persuadé que les correcteurs soient au fait de popitem et encore moins du caractère ordonné des dictionnaires alors que pendant des années on a enseigné l'inverse (quand on voit que des responsables de la partie info de concours soutenaient encore que range construisait une liste...).
Les set non plus ne sont techniquement pas au programme (mais ça peut aisément être remplacé par un dictionnaire).
Disons que j'ai tellement été refroidi par les concours que je m'efforce de ne vraiment pas marcher sur la ligne...


Pierre Karpman
1:16 PM
D'accord, merci !
(Pour les set je suis d'accord ; j'en ai utilisé un uniquement parce que c'est ce qu'il y avait dans le dfs2 du site mentionné, et je voulais le modifier le moins possible pour montrer que ça ne complexifiait pas trop la chose.) 


Pierre Karpman
1:21 PM
Pour les attendus du programme sur les dictionnaires je me suis posé la question et j'avais vérifié s'il y avait une liste exhaustive des fonctions/méthodes associées à connaître, mais ça ne me semble pas clair si les quelques exemples mentionnés dans l'annexe ont cette prétention. Bref...


g_dewaele
1:29 PM
Oui, ce sont des questions fort délicates... Je pars du principe que si une méthode n'est pas noir sur blanc dans le programme il y a un vrai risque en concours (déjà que ce qui est noir sur blanc joue de mauvais tours...). Même del, j'essaie de faire sans (mais là, pas facile de s'en passer... au moins OrderedDict a une méthode spécifique pour remonter un élément qui rend la chose plus lisible).
Note bien que ce n'est que mon ressenti, j'apprécierais que d'autres donnent le leur sur la question. Le code ne me choque pas dans l'absolu, c'est juste que dans le cadre des concours, je préfère penser la pile Python infinie et procéder par récursion pour un parcours en profondeur.


Axel Rogue
1:39 PM

Ça me semblait une suggestion assez raisonnable aussi.
Je vais conseiller de faire les niveaux 1 et 2, ça me paraît suffisant pour être serein en sup.


arnaud
3:21 PM
def DFSCycle(G, s):
    n = len(G)
    pile = [s]
    marque = [ False for _ in range(n) ]
    parents = [ None for _ in range(n) ]
    while len(pile) != 0 :
        sommet = pile.pop()
        if not marque[sommet] :
            marque[sommet] = True
            for voisin in G[sommet] :
                if parents[voisin] != None and not marque[voisin]:
                    Cycle = str(sommet)+'-'+str(voisin) +'-'+str(parents[voisin])
                    # on remonte le chemin à l'envers jusqu'à retomber sur parents[voisin]
                    while sommet != parents[voisin] :
                        sommet = parents[sommet]
                        Cycle = str(sommet)+'-'+ Cycle
                    return Cycle
                else : 
                    pile.append(voisin)
                    if not marque[voisin] :
                        parents[voisin] = sommet
    return False

def BFSCycle(G, s):
    n = len(G)
    file = collections.deque([])
    file.append(s)
    marque = [ False for _ in range(n) ]
    parents = [ None for _ in range(n) ]
    while len(file) != 0 :
        sommet = file.popleft()
        if not marque[sommet] :
            marque[sommet] = True
            for voisin in G[sommet] :
                if parents[voisin] != None and not marque[voisin]:
                    Cycle = str(sommet) + '-' + str(voisin) + '-' + str(parents[voisin])
                    voisin = parents[voisin]
                    i = 0 # gestion du choix du chemin
                    # on remonte les deux chemins à l'envers
                    while sommet != voisin :
                        if i == 0 : # chemin menant à sommet
                            sommet = parents[sommet]
                            Cycle = str(sommet) + '-' + Cycle
                        else :
                            voisin = parents[voisin]
                            Cycle = Cycle + '-' + str(voisin)
                        i = (i + 1) % 2
                    return Cycle
                else : 
                    file.append(voisin)
                    if not marque[voisin] :
                        parents[voisin] = sommet
    return False
Afficher plus
Bonjour voilà ce que j'ai écris pour les graphes non orientés. Pour le BFS j'ai reconstruit le cycle en revenant en arrière des deux côtés en même temps, jusqu'à arriver à un sommet commun. 

Je ne sais pas si c'est la bonne méthode ?


arnaud
4:19 PM

J'ai du mal à comprendre ce que fait la fonction DFS. Si marque[s]=1 elle renvoie False mais pourquoi ? La boucle for de la ligne 12 c'est pour les graphes non connexes ?


Nathaniel Carré
4:20 PM
la fonction DFS essaie de lancer un DFS depuis le sommet s ; si elle détecte un cycle, elle renvoie False, sinon elle renvoie True

effectivement, la boucle qui suit est pour être sûr de lancer un parcours sur chaque composante

4:22 PM
si marque[s] vaut 1, ça veut dire que pendant qu'on a lancé les appels récursifs sur un voisin de s, et avant qu'on les ait tous terminés, on a atteint s à nouveau, ce qui implique l'existence d'un cycle


np
4:22 PM
C'est du code astucieux que je déconseille de montrer à des élèves de la plupart des lycées :slightly_smiling_face:.


Nathaniel Carré
4:23 PM
quelle part tu considères astucieuse ? tu fais comment pour la détection de cycle orienté de ton côté ?


np
4:25 PM
if marque[s] == 0 and not DFS(s)

arnaud
4:25 PM
ça ressemble à ce qui est expliqué là:
https://info.blaisepascal.fr/nsi-parcours-dun-graphe/ 


np
4:25 PM
return marque[s] == 2
4:26 PM
Je dis juste que tu utilises des petites astuces de programmation. Pour le fond je fais pareil que toi.

4:27 PM
Alors qu'il vaudrait mieux écrire :

if marque[s] == 2:
    return True
else if marque[s] != 2:
    return False

arnaud
4:27 PM
je ne suis pas sûr que ce soit plus lisible pour les étudiants.


Nathaniel Carré
4:30 PM

je reviens sur ce code : j'ai comme un doute sur le test s == p

4:31 PM
il faudrait soit faire un test dans la boucle for du DFS, soit, comme tu le disais, utiliser un tableau de parents


np
4:34 PM
J'ai comme l'impression que quelqu'un a essayé d'adapter un code trop astucieux pour lui et s'est planté.


matthieu_solnon
5:43 PM

Oui, de mémoire on s'était dit que l'on serait très contents s'ils maîtrisaient le niveau 2 à l'entrée en PTSI et le niveau 3 à l'entrée en PT. 


g_dewaele
6:33 PM







Petite question : quel intérêt d'utiliser une vraie file (deque) pour le BFS ? Je veux dire, plutôt que :

def bfs(G, s):
    parents = {s: None}
    file = [s]
    idx = 0
    
    while idx < len(file):
        v = file[idx]
        for w in G[v]:
            if w not in parents:
                parents[w] = v
                file.append(w)
        idx += 1
    
    return parents