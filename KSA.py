#!/usr/bin/python

"""
   	A tool for implementing a generalised suffix tree from the paper "Space - efficient k-mer search algorith for the Generalised 	      Suffix Tree" by Freeson Kaniwa et. al. 
	The class  with methods adds, search, and startsWith methods.
	This tool was tested on Ubuntu 14.04LTS and runs with Python 3.5.2 and Anaconda 4.1.1 (64bit) 
	Instructions for running the tool:
		1) To calculate the memory usage - download the 'memusg' tool from github (check the reference given in the paper) 
		2) Run the tool with 'memusg' to get the peak memory usage of the tool
		3) Run the tool with linux time command to get the running time of the tool
		

"""
import subprocess
import collections
import os


class Generalised_Suffix_Tree:
    
    def __init__(self):
        self.root = collections.defaultdict()

 
    def add(self, substring):  # adds a substring in to the tree
        current = self.root
        for character in substring:
            current = current.setdefault(character, {})
        current.setdefault("$")   # adds a terminal symbol to each substring in to the tree

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def _prefix_(self, prefix):   # not necessary but can be used to find or search a prefix
        current = self.root
        for character in prefix:
            if character not in current:
                return False
            current = current[character]
        return True

    def search(self, pattern): # takes pattern as a string parameter
        current = self.root
        for character in pattern:
            if character not in current:
                return False  # returns boolean false if not found
            current = current[character]
        if "$" in current:
            return True  # returns boolean true if not found
        return False

   
# Now test the class
#os.system('stat -c%s dna.fa > size.txt')
#with open('size.txt','r') as file1:
#		file_size=int(file1.readline())

if __name__=="__main__":
	p = subprocess.Popen("stat -c%s dna.fa", stdout=subprocess.PIPE, shell=True)  #@dna.fa - you specify the textfile to be read or indexed to calculate the size of the file
	(file_size, err) = p.communicate()

	file_size=int(file_size)-1

	pattern='TAAAAT'			#speficy the repeat or pattern to be searched here - the repeat also detects the size of the tree and the value K so the tree will be of K height

	repeat1='TAAAATCAAACTTAAAATCAAACTTAAAATCAAACTTAAAATCAAACTTAAAATCAAACTTAAAATCAAACT'  # not necessary, its for testing purposes

	k=len(pattern)

	gst = Generalised_Suffix_Tree()

	data=[]

	n = (int(file_size)-k)+1
	with open('dna.fa','r') as myfile:	#@dna.fa - you specify the textfile to be read or indexed
			data=myfile.read()
	#print ('n is',n)
	#print data1
	for i in range(n):		
		
			#myfile.seek(i)
			#sub=myfile.read()# Go to the 3rd byte before the end
			gst.add(data[i:i+k])    #  @data[i:i+k] the sliding window size which is being moved one character at a time by the for-loop
			#print data1[i:i+repeat_size]
		

	print ('Completed construction')   #Confirmation if reading and indexing is done
	print (gst.search(pattern))  # Boolean output showing the presence of the repeat

