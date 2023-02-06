from draw import * # la fonction dessine représente l´arbre en console
from file import *
from pile import *

# notre classe Node
class Node():
    def __init__(self, val):
        self.val = val
        self.gauche = None
        self.droit = None

    def __repr__(self):
        if self==None:
            return
        return "["+str(self.val)+","+str(self.gauche)+","+str(self.droit)+"]"

# exercice 1
def hauteur (arbre):
    if arbre==None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche),hauteur(arbre.droit))
    
# exercice 2
arbre1 = Node('Dom Manuel')
arbre1.gauche = Node('Fernando')
arbre1.droit = Node('Beatriz')
arbre1.droit.droit = Node('Isabel de Barcelos')
arbre1.gauche.gauche = Node('Duarte I')
arbre1.gauche.droit = Node('Leonor d´Aragon')
arbre1.droit.gauche = Node('João Cond.')
arbre1.droit.gauche.droit = Node('Filipa de Lancastre')
arbre1.droit.gauche.gauche= Node('Dom João I')
# dessine(arbre1)

# exercice 3
arbre2=Node(1)
arbre2.gauche=Node(2)
arbre2.gauche.gauche=Node(3)
arbre2.gauche.droit=Node(4)
arbre2.gauche.droit.gauche=Node(5)
arbre2.gauche.droit.droit=Node(6)
arbre2.droit=Node(7)
arbre2.droit.gauche=Node(8)
arbre2.droit.droit=Node(9)
# dessine(arbre2)


# exercice 4
def operateur(c):
    if c=='+' or c=='-'or c=='*'or c=='/':
        return True
    else:
        return False
    
def calculer(a,b,op):
    if op=='+':return a+b
    if op=='-':return a-b
    if op=='*':return a*b
    if op=='/':
        if b!=0:return a/b
        else: print("erreur de division par zero")
        
def rpn(expression):
    p=Pile() # creer_pile
    for e in expression:
        if operateur(e):# si un opérateur a été trouvé
            a=p.sommet.element  # on stocke l'élément de sommet de P dans la variable a
            p.depiler()  # on dépile P
            b=p.sommet.element # on stocke l'élément de sommet de P dans la variable b
            p.depiler()
            r=calculer(b,a,e) # on calcule l'opération trouvée
            p.empiler(r) # on empile P avec le résultat              
        else: 
            p.empiler(int(e)) # on empile le nombre de l'expression             
    return p.sommet.element


arbre3=Node('*')
arbre3.gauche=Node('-')
arbre3.gauche.gauche=Node('/')
arbre3.gauche.droit=Node('1')
arbre3.gauche.gauche.gauche=Node('6')
arbre3.gauche.gauche.droit=Node('-')
arbre3.gauche.gauche.droit.droit=Node('1')
arbre3.gauche.gauche.droit.gauche=Node('3')
arbre3.droit=Node('+')
arbre3.droit.gauche=Node('3')
arbre3.droit.droit=Node('2')
dessine(arbre3)


liste=[]
def postfixe(arbre):
    if arbre==None:
        return
    else:
        postfixe(arbre.gauche)
        postfixe(arbre.droit)
        liste.append(arbre.val)
        
# exercice 5
def prefixeIter(arbre):     
    if arbre is None:
        return
    p=Pile()
    p.empiler(arbre)
    while(not p.est_vide()):
        node = p.depiler()
        print (node.val, end=" ")
        # On empile les fils gauche et droits du noeud dépilé si ils existent
        if node.droit is not None:
            p.empiler(node.droit)
        if node.gauche is not None:
            p.empiler(node.gauche)


    