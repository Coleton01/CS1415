"""
Chapter8: Election program GUI modification
Coleton Hardenbrook and Landon Dahl
Date:11/7/2020
Objective: convert previous election program into a GUI
"""

from breezypythongui import EasyFrame

import random

class election(EasyFrame):
    

    def __init__(self):

        EasyFrame.__init__(self,"election counter")
        self["background"] ="gray"
        
        #fields for input of candidate name
        self.candidates= self.addLabel(text="Candidate name:",row=0,column=0)
        self.candidate2= self.addLabel(text="2nd candidate name:" ,row=1,column=0)
        self.candidate3= self.addLabel(text="3rd Candidate name:",row=2,column=0)

        #text inputs
        self.c1= self.addTextField(text="",row=0, column=1)
        self.c2= self.addTextField(text="",row=1,column=1)
        self.c3= self.addTextField(text="",row=2,column=1)


       
        #Buttons
        self.b1=self.addButton(text="vote", row =3, column=1, command=self.votes)
        self.b2=self.addButton(text="clear", row =3, column=0, command=self.clear)
        self.b3=self.addButton(text="tally",row=5,column=0,command=self.electionResults)


        #text area for generating votes:
        self.results=self.addTextArea("", row=4, column=0, columnspan=2, width=50, height=15)

        #results area:
        self.counts=self.addTextField("",row=6,column=0,columnspan=2,width=100,state="readonly")
        
        self.v1=self.addLabel(text="Number of votes for candidate 1:", row =7,column=0)#labels
        self.v2=self.addLabel(text="Number of votes for candidate 2:", row =8,column=0)
        self.v2=self.addLabel(text="Number of votes forcandidate 3:", row =9,column=0)

        self.v1a=self.addTextField("", row=7, column=1,state="readonly")#outputfields
        self.v2a=self.addTextField("", row=8, column=1,state="readonly")
        self.v3a=self.addTextField("", row=9, column=1,state="readonly")

        
        
    def votes(self):
        """This program will cast 100 random votes to a text file."""
        #retrieve candidate names
        candidate1=self.c1.getText()
        candidate2=self.c2.getText()
        candidate3=self.c3.getText()
        CandidateList=[candidate1, candidate2,candidate3]

        
        v= open("C:/Users/coled/Documents/School/Fall 2020/Fundamentals of programming/Project B/2020votes.txt", 'w')
        for x in range(0,1000):
            voterChoice= random.choice(CandidateList)  ##random choice of list of candadites is appened to .txt
            v.write(voterChoice)
            v.write("\n")
        v.close()

        #display votes in text field
        FList=[("python Files", "*.py"), ("Text files", "*.txt")]
        fileName="C:/Users/coled/Documents/School/Fall 2020/Fundamentals of programming/Project B/2020votes.txt"
        if fileName != "":
            file=open(fileName,'r')
            text=file.read()
            file.close()
            self.results.setText(text)
            self.setTitle(fileName)

    def electionResults(self):
        """This program will satisfy requirements for #2: a,b,c and D of project B.  It will read votes from a .txt file
    tally all votes using count and append. Display the total votes for each category and declar a winner. """
#count variables for name incrementation
        count=0
        countCandidate1=0
        countCandidate2=0
        countCandidate3=0
#list of candidate names for tally
        candidate1=self.c1.getText()
        candidate2=self.c2.getText()
        candidate3=self.c3.getText()

        f=open("C:/Users/coled/Documents/School/Fall 2020/Fundamentals of programming/Project B/2020votes.txt", 'r')

        electionList= f.read().splitlines()    #read file input and splits by newline character
    
    
        for line in electionList:               #sorts through list and increments to variables based on string characters
            count+=1
            if line == candidate1:
                countCandidate1 +=1
            elif line == candidate2:
                countCandidate2 +=1
            elif line == candidate3:
                countCandidate3 +=1

            
    #### outtputs of program###      
    #print("The total votes cast in this election:",count,"| Biden's total votes:", countBiden, "| trump's total votes:",countTrump, "| Hardenbrook's total votes: ",countHardenbrook)


    #if statesments to declare winners or ties based on election counts#
        if (countCandidate1 > countCandidate2)  and (countCandidate2 > countCandidate3):
            message=" With a total of", countCandidate1,"votes.",candidate1," is the winner!!!!"
        if (countCandidate2 > countCandidate1)  and (countCandidate2 > countCandidate3):
             message=" With a total of", countCandidate2,"votes.",candidate1," is the winner!"
        if (countCandidate3 > countCandidate1)  and (countCandidate3> countCandidate1):
            message=" With a total of", countCandidate3,"votes.", candidate3,"is the winner!!!!"
        if (countCandidate3 == countCandidate2)  or (countCandidate3==countCandidate2) or (countCandidate1==countCandidate2):
            message=" A Tie has been declared! We will redo the election"


        #output to text fields:
        self.counts.setText(message)
        self.v1a.setText(countCandidate1)
        self.v2a.setText(countCandidate2)
        self.v3a.setText(countCandidate3)
        
        
            



    def clear(self):
        self.results.setText("")
        self.c1.setText("")
        self.c2.setText("")
        self.c3.setText("")
        self.counts.setText("")
        self.v1a.setText("")
        self.v2a.setText("")
        self.v2a.setText("")    
    

        


        



def main():
    election().mainloop()


main()
