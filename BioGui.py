"""
Final project: DNA Splice and convert
Coleton Hardenbrook
This file is the dedicated graphics portion of my project.
It will contain a file input, convert button, text area.
"""

from breezypythongui import EasyFrame
import random
from tkinter import *
import webbrowser
import tkinter.filedialog
import bio_data_management
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#global variables
#seq_record=''

class Window(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self, "Biopython GUI")
        self["background"] = "gray"
        #url= "https://www.ncbi.nlm.nih.gov/genome/"
        #new=1
        list
        Dictionary={'welcome':'Welcome to the Biopython Gui! We will be able to display information about your downloaded DNA file. We will also be able to provide data manipulation with these files.',
                    'Instructions':'Please use the below buttons to dictate what you would like to do with your file and data!'}
        
   

    #panel-1
        buttonPanel= self.addPanel(row=0,column=0, columnspan=2, background='gray')

        buttonPanel.addLabel(text=Dictionary['welcome'], row=0,column=0,columnspan=4,sticky=N+S+W+E)
        buttonPanel.addButton(text="Please select a file of type Fasta to load", row =1, column=0, command=self.LoadFile)

        buttonPanel.addButton(text="Find DNA- will take you to external database",row =1, column=1, command=self.BlastDirectory)
        buttonPanel.addButton(text='                 clear entry                ', row=1,column=2, command=self.New)
    #panel-2
        buttonPanel2=self.addPanel(row=1,column=0,background='gray')
        self.results= buttonPanel2.addTextArea("", row=0, column=0, columnspan=2, width=50, height=15)
        buttonPanel2.addLabel(text='Statistics of your genome:', row=1, column=0)
        buttonPanel2.addLabel(text='GC percentage:', row=2, column=0)
        buttonPanel2.addLabel(text='geneome Length', row=3, column=0)
        self.gcResults=buttonPanel2.addFloatField(value=0 ,row=2, column=1)
        self.lenResults=buttonPanel2.addFloatField(value=0 ,row=3, column=1)

    #panel 3
        buttonPanel3=self.addPanel(row=2,column=0,background='gray')
        buttonPanel3.addLabel(text=Dictionary['Instructions'], row=0,column=0,columnspan=4,sticky=N+S+W+E)
        self.TransResults=buttonPanel3.addButton(text='translate/transcribe', row=1,column=0)
        self.ConvertResults=buttonPanel3.addButton(text='convert to different file type',row=1,column=1)
        

        
    #methods
    def BlastDirectory(self):
        """will direct to blast/ncbi website for genome search"""
        webbrowser.open("https://www.ncbi.nlm.nih.gov/genome/", new=2)
        
    def LoadFile(self):
        """this function offers the ability to load a file. """
        
        fList= [("FASTA files", "*.fasta*"),("Genbank File", "*.gbk*"),("Text Files", "*.txt.") ] #list for possible file types

        fileName= tkinter.filedialog.askopenfilename(parent=self, filetypes=fList)
        
        list1=[]
        if fileName != "":
            if ".fasta" in fileName:
            
        #loops through file and seperates genes/chromosomes by id and sequence
                for seq_record in SeqIO.parse(fileName, "fasta"):
                    list1+= "Identifcation= " +seq_record.id +'\n', "SEQUENCE="+seq_record.seq + '\n' +'\n'

            elif ".gbk" in fileName:
                for seq_record in SeqIO.parse(fileName,'genbank'):
                    list1+= "Identifcation= " +seq_record.id +'\n', "SEQUENCE="+seq_record.seq + '\n'
                
                
                
            #print variable to see collected data
            self.results.setText(list1)

            #set file to seq object for data manipulation
          

            
    def New(self):
        """this will clear the current text field and input fields"""
        #self.inputfieldopen.setText("")
        self.results.setText("")
            
            
            
            
           

    def FileConverter(self):
        
        pass
        
       
        
        

    ###possible text area and image match via dictionary


def main():
    Window().mainloop()


main()
