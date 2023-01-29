class Noeud:
    def __init__(self, element, suivant=None):
        self.element = element
        self.suivant = suivant

class Pile:
    def __init__(self):
        """Crée une pile vide"""
        self.sommet=None
    def __len__(self):
        """Donne la taille de la pile"""
        courant = self.sommet
        cpt = 0
        while courant != None:
            courant = courant.suivant
            cpt += 1
        return cpt
    def est_vide(self):
        """Vérifie si la pile est vide"""
        if self.sommet == None:
            return True
        else:
            return False

    def empiler(self, element):
        """Ajoute un élément sur le sommet de la pile"""
        if self.sommet == None:
            self.sommet=Noeud(element)      
        else:
            nouveau = Noeud(element)
            nouveau.suivant = self.sommet
            self.sommet = nouveau
            
    def depiler(self):
        """Enlève et renvoie l'élément situé sur le sommet de la pile"""
        if self.est_vide():
            return 'La pile est vide!'      
        else:
            # Enlève le noeud au sommet
            # le précédent est le nouveau sommet
            noeud_efface = self.sommet
            self.sommet = self.sommet.suivant
            noeud_efface.suivant = None
            return noeud_efface.element
    def __repr__(self):        
        courant = self.sommet
        ch=''
        if self.est_vide():
            return "La pile est vide!"
        else:
            while(courant != None):
                ch+=("|\t"+str(courant.element)+"\t|\n")
                courant = courant.suivant
            return ch