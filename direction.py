# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:09:02 2018

@author: Brunel
"""

    def up(self):
       """Deplacement de une case vers le haut"""
       for i in [1,2,3]:
           for j in range(4):
               if self.plateau[i,j] != 0:
                   self.plateau[i-1,j] = self.plateau[i,j]
                   self.plateau[i,j] = 0
                   
    def left(self):
        self.plateau = np.transpose(self.plateau)
        self.up()
        self.plateau = np.transpose(self.plateau)
    
    def  down(self) :
        self.plateau = self.plateau[[3,2,1,0],:]
        self.up()
        self.plateau = self.plateau[[3,2,1,0],:]
    
    def right(self) :
        self.plateau = np.transpose(self.plateau)
        self.down()
        self.plateau = np.transpose(self.plateau)