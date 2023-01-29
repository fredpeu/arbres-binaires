class File:
    
    def __init__(self):
        self.file = []

    def enfiler(self, element):
        self.file.append(element)

    def defiler(self):
        if self.file:
            return self.file.pop(0)

    def estVide(self):
        return self.file == []
    
    def queue(self):
        if not self.estVide():
            return self.file[-1]
        else: return 'La file est vide'
    
    def tete(self):
        if not self.estVide():
            return self.file[0]
        else: return 'La file est vide'

    def __len__(self):
        return len(self.file)

    def __repr__(self):
        ch = "\nEtat de la file:\n<--| "
        for x in self.file:
            ch +=  str(x) + " | "
        return ch
