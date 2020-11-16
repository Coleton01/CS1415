"""
Chapter 9: project 9
Coleton Hardenbrook and Landon Dahl
Date: 11/13/2020
objective: we will be creating the Card demo program.
"""
import random
from breezypythongui import EasyFrame
from cards import Card, Deck
from tkinter import PhotoImage

class CardDemo(EasyFrame):

    def __init__(self):
        """Creates the cards and sets up the images and labels for two cards
to be displayed, the state label, and two command buttons. """
        EasyFrame.__init__(self, title="Card Game")
        self.setSize(220,200)

        #create cards/deck
        self.card1=Deck()
        self.card="b"
        
      
        

        #labels
        self.cardLabel1= self.addLabel("",row=0, column=0, sticky= "NSEW",columnspan=2)
        
        self.stateLabel = self.addLabel(self.card, row = 1, column = 0,
                                        sticky = "NSEW",
                                        columnspan = 2)
        
        self.addButton(row = 2, column = 0,
                       text = "Draw",
                       command = self.nextDraw)
        
        self.addButton(row = 2, column = 1,
                       text = "New game",
                       command = self.newGame)
        
        self.refreshImages()

    def nextDraw(self):
        """draws a card and updates view"""
        self.card=self.card1.deal()
        self.stateLabel = self.addLabel(self.card, row = 1, column = 0,
                                        sticky = "NSEW",
                                        columnspan = 2)
        #call split of rank and suite
        self.convert()
        
        
       
        #self.refreshImages()
        
    def newGame(self):
        self.card1=Deck()
        self.card1.shuffle()
        self.stateLabel["text"]=""
        self.card="b"
        self.refreshImages()

    def refreshImages(self):
        """updates the images in the window"""
        
        
        fileName1="DECK/" + str(self.card) + ".gif"
        self.image1= PhotoImage(file=fileName1)
        self.cardLabel1["image"]= self.image1
        

    def convert(self):
        """converts the strin created from .deal and changes it into
a format for finding image files. """
        rank=''
        suits=''
        x=str(self.card)
        self.newWordList=x.split()
        print(self.newWordList)

        #if statements to change word for image path
        if self.newWordList[0] == 'Ace':
            rank = '1'
        elif self.newWordList[0] == 'Jack':
            rank = '11'
        elif self.newWordList[0] =='Queen' :
            rank = '12'
        elif self.newWordList[0] == 'King':
            rank = '13'
        else:
            rank = self.newWordList[0]
        
    

        if self.newWordList[2] == 'Spades':
            suits = 's'
        elif self.newWordList[2] == 'Hearts':
            suits = 'h'
        elif self.newWordList[2] =='Diamonds' :
            suits = 'd'
        elif self.newWordList[2] == 'Clubs':
            suits = 'c'

        name=rank+suits
        print(name)
                   
        self.card=rank+suits
        self.refreshImages()
        
        
        
        
def main():
    CardDemo().mainloop()


main()
                    
        

        
