#!/usr/bin/python

"""
   	A tool for implementing a generalised suffix tree from the paper "Space - efficient k-mer search algorith for the Generalised Suffix Tree" by Freeson Kaniwa. 
	The class  with methods adds, search, and startsWith methods.
	This tool was tested on Ubuntu 14.04LTS and runs with Python 3.5.2 and Anaconda 4.1.1 (64bit) 
	Instructions for running the tool:
		1) To calculate the memory usage - download the 'memusg' tool from github (check the reference given in the paper) 
		2) Run the tool with 'memusg' to get the peak memory usage of the tool
		3) Run tge tool with linux time command to get the running time of the tool
		

"""
import subprocess
import collections
import os
import multiprocessing
from timeit import default_timer

lock=multiprocessing.Lock()

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

def sub_tree(var):
	#global data
	global gst
	global k
	gst = Generalised_Suffix_Tree()
	for i,item in enumerate(data):		
		if item==var:
			lock.acquire()
			gst.add(data[i:i+k])
			lock.release()
	print (gst._prefix_(pattern))


if __name__=="__main__":
	global data
	data=[]
	p = subprocess.Popen("stat -c%s test.fa", stdout=subprocess.PIPE, shell=True)  #@dna.fa - you specify the textfile to be read or indexed to calculate the size of the file
	(file_size, err) = p.communicate()

	file_size=int(file_size)-1

	pattern='CCCAA'			#speficy the repeat or pattern to be searched here - the repeat also detects the size of the tree and the value K so the tree will be of K height

	repeat1='CCTAACCCTAACCCTAACCCTAACCCCTAACCCCTAA'  # not necessary, its for testing purposes

	k=len(pattern)

	n = (int(file_size)-k)+1
	#n = int(file_size)
	with open('test.fa','r') as myfile:	#@dna.fa - you specify the textfile to be read or indexed
			data=myfile.read().replace('\n','')
	#sub_tree_T()
	start = default_timer()
	Alphabet=['A','C','G','T']
	p=multiprocessing.Pool(4)
	p.map(sub_tree,Alphabet)	
	p.close()
	p.join()
	print ('Completed construction')   #Confirmation if reading and indexing is done
	duration = default_timer() - start
	print ('Construction time : ', duration)
	#print (gstT.search(pattern))  # Boolean output showing the presence of the repeat

