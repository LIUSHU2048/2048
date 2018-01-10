# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:49:47 2018

@author: 3404503
"""

import numpy as np

    def pop(self) :
        """Cette méthode crée une nouvelle case de valeur aléatoire entre 2 et 4 à une position aléatoire sur le plateau"""
        a = np.random.randint(1,3)
        valeur = 2*a
        x = 0
        y = 0
        while self.plateau[x,y] != 0:            
            x = np.random.randint(0,4) 
            y = np.random.randint(0,4)
        self.plateau[x,y] = valeur
        print(self.plateau)