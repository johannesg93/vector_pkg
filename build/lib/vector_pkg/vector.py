import numpy as np

class Vector:
    """
    ich bin ein vektor OIDA
    """
    
    def __init__(self, components):
        self.components = components
        
    
    def length(self):
        #selbst erstellter docstring
        """
        heast oida. diese methode rechnet die länge eines vektors aus. bam!
        """
        l = np.sqrt((self.components[0]**2) + (self.components[1]**2) + (self.components[2]**2))
        return l
    
    def dotp(self, boi2):

        #wow, man kann docstrings generieren lassen!! folgendes kommt dabei raus:
        #das is numpy style oida
        """


        Parameters
        ----------
        boi2 : bitte nur listen mit 3 komponenten. sonst krachts leider :/
            der 2. vektor, mit dem man den inputvektor skalarmultiplizieren will.

        Returns
        -------
        dp : float (hoffe ich zumindest)
            ergebnis der rechnung.

        """
        dp = 0
        for i in range(0,3):
            dp = dp + self.components[i]*boi2[i]
        return dp
    
    
    def crossp(self, boi2):
        cp = 0
        cp = [self.components[1]*boi2[2] - self.components[2]*boi2[1], self.components[2]*boi2[0] - self.components[0]*boi2[2], self.components[0]*boi2[1] - self.components[1]*boi2[0]]
        return Vector(cp)