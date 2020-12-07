"""
File: DNA manipulation
Coleton Hardenbrook
this file will contain various functions in order to manipulate data generated
from the DNA sequence
"""

import Bio
from Bio.SeqUtils import GC
from Bio import SeqIO



#will create appropriate class

class DNAdata:

    def __init__(self, sequence):
        self.sequence=sequence

    
    
    def percentGC(self):
        """this function will calculate the GC content of a strand of DNA"""

        my_seq  = self.sequence
        GCstate = GC(my_seq)
        print(GCstate)

    def Trans_Trans(self):
        """This function will transcribe and translate a string of DNA into a string of RNA"""

        coding_dna = seq(self)
        print("your coding strand is:", coding_dna)

    #translates coding strand into template strand
        template_dna = coding_dna.reverse_complement()
        print("your template strand", template_dna)

    #transcribe coding strand to mRNA
        messenger_rna = template_dna.reverse_complement().transcribe()
        print(messenger_rna)

    #translates sequence to protein
    
        messenger_rna.translate()
        print(messenger_rna)


    

    
    def Import(self):
        """imports file types of FASTA, and genbank.
        Saves to a variable after assigning string type"""
        pass

      




def main():
   x=DNAdata("AGTC")
   x.percentGC()



main()


        

        
        
