from capytale.autoeval import (
    Validate,
    ValidateVariables,
    ValidateFunction,
    ValidateFunctionPretty,
)
from itertools import product
import random as rd




def make_liste_chaine():
    """
    ["kjqsdfqsjf","lksdjflkjf",...]
    """
    vtt = [[chr(rd.randrange(34,125)) for _ in range(30)] for i in range(10)]
    vt = []
    for l in vtt :
        ch = ""
        for c in l :
            ch += c
        vt.append(ch)
    return vt

def make_liste_chaine_chr():
    """
    [("e","skdmqlksdmqskl"),]
    """
    vtt = [[chr(rd.randrange(34,125)) for _ in range(30)] for i in range(10)]
    vt = []
    for l in vtt :
        ch = ""
        for c in l :
            ch += c
        vt.append((ch,chr(rd.randrange(34,125))))
    return vt

def make_liste_chaine_chaine():
    """
    [("skdmqlksdmqskl","skdmqlksdmqskl"),]
    """
    vtt1 = [[chr(rd.randrange(34,125)) for _ in range(30)] for i in range(10)]
    vtt2 = [[chr(rd.randrange(34,125)) for _ in range(30)] for i in range(10)]


    vt1 = []
    vt2 = []
    for l in vtt1 :
        ch = ""
        for c in l :
            ch += c
        vt1.append(ch)
    for l in vtt2 :
        ch = ""
        for c in l :
            ch += c
        vt2.append(ch)

    vt = [(vt1[i],vt2[i]) for i in range(len(vt1))]
    return vt


def make_liste_chr_chaine():
    """
    [("skdmqlksdmqskl","e"),]
    """
    vtt = [[chr(rd.randrange(34,125)) for _ in range(30)] for i in range(10)]
    vt = []
    for l in vtt :
        ch = ""
        for c in l :
            ch += c
        vt.append((chr(rd.randrange(34,125)),ch))
    return vt


def ratio_justes(L):
    '''renvoie le nombre de tests justes ramené sus forme d'un ratio
    3 tests justes sur 4 renverra 0.75'''
    try:
        nt=len(L)
        s=0
        for e in L:
            if e[3]==True :
                s=s+1
        r=s/nt
    except : #l'éleve n'a pas eu de tests car sa fonction n'était pas définie
        r=0
    return(r)

def evaluation(e):
    """
    si e=0 affiche la note brute ;
    si e=1 affiche la note sur 20,
    si e=2 affiche le détail  ;
    si e=3 fait tous les tests (si l'éléve ne les a pas fait et affiche la note /20
    """

    if e==3:
        for _Q, _v in tests_Q.items():
            _v[0]()


    surx=20 #pour changer note /20 : /10 ...

    points={}
    note = 0
    tot=0
    for _Q, _v in tests_Q.items():
        #_Q , nom du test
        #_v : validate[0]
        #_v : validate[1] : questions
        #print(_v)
        #_d=_donneeT[_Q]
        _d=_v[1]


        #if _d[3]=="V": #il s'agit d'un test de variable
        if _d['type_test']=="variable": #il s'agit d'un test de variable
            if _v[0]._validated==True:
                points[_Q]=_d[4]   #_d[4] contient le nombre de points affectés à la question
            else:
                points[_Q]=0

        else : #il s'agit d'un test de fonction
            if _v[0]._validated==True:
                #points[_Q]=_d[4]  #on donne le nombre de points maxi
                points[_Q]=_d['pts_max']  #on donne le nombre de points maxi
            else :
                points[_Q]=ratio_justes(_v[0]._test_results)*_d['pts_max']
                        #on donne le nombre de points proportionnels au nombre de tests réussis
        note = note+points[_Q]
        tot = tot+_d['pts_max']

    if e==0:
        print("Note : "+str(note)+" / "+ str(tot))


    if e==1 or e==3:
        print("Note : "+str(round(note/tot*surx,1))+" / "+ str(surx))


    if e==2:
        for _Q, _v in tests_Q.items():
            print(_Q+" : "+str(points[_Q])+" / "+str(_donneeT[_Q][4]))
        print("\n")
        print("Note : "+str(note)+" / "+ str(tot))




##
def _cor_moyenne_q1(a:list) -> float :
    return sum(a)/len(a)

vt = [[rd.randrange(-50,50) for _ in range (rd.randrange(1,20))] for i in range(10)]
cibles = [_cor_moyenne_q1(l) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"moyenne",
            "f_corr" :_cor_moyenne_q1,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions = [question]

##
def _cor_variance_q2(a:list) -> float :
    m = _cor_moyenne_q1(a)
    l = [(x-m)**2 for x in a]
    return sum(l)/len(l)

vt = [[rd.randrange(-50,50) for _ in range (rd.randrange(1,20))] for i in range(10)]
cibles = [_cor_variance_q2(l) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"variance",
            "f_corr" :_cor_variance_q2,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_maximum_q3(a:list) -> float :
    return max(a)

vt = [[rd.randrange(-50,50) for _ in range (rd.randrange(1,20))] for i in range(10)]
cibles = [_cor_maximum_q3(l) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"maximum",
            "f_corr" :_cor_maximum_q3,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_majores_par_q4(L,x):
    nb = 0
    for v in L :
        if v >= x :
            nb = nb + 1
    return nb

vt = [([rd.randrange(-50,50) for _ in range (rd.randrange(1,20))],rd.randrange(1,20)) for i in range(10)]
cibles = [_cor_majores_par_q4(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"majores_par",
            "f_corr" :_cor_majores_par_q4,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_elements_majores_par_q5(a:[],x) -> float :
    maj = []
    for v in a :
        if v < x :
            maj.append(v)
    return maj

vt = [([rd.randrange(-50,50) for _ in range (rd.randrange(1,20))],rd.randrange(1,20)) for i in range(10)]
cibles = [_cor_elements_majores_par_q5(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"elements_majores_par",
            "f_corr" :_cor_elements_majores_par_q5,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_sequentielle_q6(a:[],x) -> float :
    return x in a

vt = [([rd.randrange(-50,50) for _ in range (rd.randrange(1,20))],rd.randrange(1,20)) for i in range(10)]
cibles = [_cor_sequentielle_q6(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"sequentielle",
            "f_corr" :_cor_sequentielle_q6,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)


##
def _cor_index_sequentielle_q7(a:[],x) -> float :
    for i in range(len(a)):
        if a[i] == x :
            return i
    return -1

vt = [([rd.randrange(-50,50) for _ in range (rd.randrange(1,20))],rd.randrange(1,20)) for i in range(10)]
cibles = [_cor_index_sequentielle_q7(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"index_sequentielle",
            "f_corr" :_cor_index_sequentielle_q7,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_occurenceElement_q8(a:[],x) -> float :
    for i in range(len(a)):
        if a[i] == x :
            return i
    return -1

vt = [([rd.randrange(-50,50) for _ in range (rd.randrange(1,20))],rd.randrange(1,20)) for i in range(10)]
cibles = [_cor_occurenceElement_q8(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"occurenceElement",
            "f_corr" :_cor_occurenceElement_q8,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_occurenceElement_q8(a:[],x) -> float :
    nb = 0
    for v in a :
        if v == x :
            nb = nb +1
    return nb

vt = [([rd.randrange(-50,50) for _ in range (rd.randrange(1,20))],rd.randrange(1,20)) for i in range(10)]
cibles = [_cor_occurenceElement_q8(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"occurenceElement",
            "f_corr" :_cor_occurenceElement_q8,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

# ##
# def _cor_occurenceListe_q9(a:[]) :
#     L = [0]*(max(a)+1)
#     for v in a :
#         L[v] = L[v] + 1
#     return L
#
# vt = [[rd.randrange(0,50) for _ in range (rd.randrange(1,20))] for i in range(10)]
# cibles = [_cor_occurenceListe_q9(l) for l in vt]
# question = {"type_test": "pretty",#valeur,pretty, normal
#             "f_eleve":"occurenceListe",
#             "f_corr" :_cor_occurenceListe_q9,
#             "valeur_test" : vt,
#             "valeur_cible" : cibles,
#             "pts_max" : len(vt)}
#
# questions.append(question)



##
def _cor_affiche_voyelle_last_q14(mot) :
    voyelles = 'aeiouyAEIOUY'
    index = -1
    for i in range(len(mot)) :
        if mot[i] in voyelles :
            index = i
    return index

vt = make_liste_chaine()
cibles = [_cor_affiche_voyelle_last_q14(l) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"affiche_voyelle_last",
            "f_corr" :_cor_affiche_voyelle_last_q14,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_indice_lettre2_q16(c,mot) :
    index = -1
    for i in range(len(mot)) :
        if mot[i] == c :
            index = i
    return index

vt = make_liste_chr_chaine()
cibles = [_cor_indice_lettre2_q16(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"indice_lettre2",
            "f_corr" :_cor_indice_lettre2_q16,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_is_egal_q17(mot1,mot2) :
    return mot1 == mot2

vt = make_liste_chaine_chaine()
cibles = [_cor_is_egal_q17(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"is_egal",
            "f_corr" :_cor_is_egal_q17,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)

##
def _cor_indice_diff_q18(mot1,mot2) :
    if len(mot1) == len(mot2) :
        for i in range(len(mot1)) :
            if mot1[i] != mot2[i] :
                return False
        return True
    return False

vt = make_liste_chaine_chaine()
cibles = [_cor_indice_diff_q18(l[0],l[1]) for l in vt]
question = {"type_test": "pretty",#valeur,pretty, normal
            "f_eleve":"indice_diff",
            "f_corr" :_cor_indice_diff_q18,
            "valeur_test" : vt,
            "valeur_cible" : cibles,
            "pts_max" : len(vt)}

questions.append(question)




tests_Q = {}
for q in questions :
    if q["type_test"] == "variable" :
        tests_Q[q["f_eleve"]] = (ValidateVariables({q["valeur_test"]:q["valeur_cible"]}),q)

    elif q["type_test"] == "pretty" :
        tests_Q[q["f_eleve"]] = (ValidateFunctionPretty(q["f_eleve"],q["valeur_test"],valid_function=q["f_corr"]),q)

    elif q["type_test"] == "normal" :
        tests_Q[q["f_eleve"]] = (ValidateFunction(q["f_eleve"],q["valeur_test"],valid_function=q["f_corr"]),q)

