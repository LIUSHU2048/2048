# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:50:32 2018

@author: 3404503
"""


    def __init__(self):
        """la grille initiale est un tableau 4x4 de zero (absance de boite)"""
        self.plateau = np.zeros(16).reshape(4,4)