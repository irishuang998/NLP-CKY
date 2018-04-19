#imports
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
#looks like a dictionary of String: list[string] is easy

def import_grammer_from_file(file_name):
	grammer_file = open(file_name,'r')
	grammer = {}
	#read file
	for line in grammer_file:
		split_line = line.strip('\n').split('->')
		grammer[split_line[0].strip(' ')] = [word.strip(' ') for word in split_line[1].split('|')]

	return grammer

	#put into structure 
	#return grammer for later use
def CFG_to_CNF(grammer):
	for key,val in grammer.items():
		#print(key,val)
		#1: Check right side S and add S' to production
		a = ['S' in product.split(' ') for product in val]
		if any(a):
			grammer['S^']=['S'] 
			break
		#2 Remove NULL production
		#3 Remove Unit production
		#4 Remove More than 2 production

		#current example already in CNF form
	return grammer
def CKY_parse(sentence,cnf_grammer):
	x1     =[]
	y1     =[]
	color1 =[]
	text1  =[]#only can have text, the other all have just color
	x2     =[]
	y2     =[]
	color2 =[]
	x3     =[]
	y3     =[]
	color3 =[]
	split_sentence = sentence.split(' ');
	length=len(split_sentence)
# 	#dynamic programming
# 	let the input be a string I consisting of n characters: a1 ... an.
# let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
	mat = [[ [] for x in range(length)] for y in range(length)] 
# let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
# for each s = 1 to n
	for s in range (length):	

		for key, value in cnf_grammer.items():
			
			if '\''+split_sentence[s]+'\'' in value:
				mat[length-1][s].append(key)
	print_mat(mat)
#   for each unit production Rv -> as
#     set P[1,s,v] = true

# for each l = 2 to n -- Length of span
	for l in range(2,length+1):
#   for each s = 1 to n-l+1 -- Start of span
		for s in range(0,length-l+1):
#     for each p = 1 to l-1 -- Partition of span
			for p in range(1,l):
				for key, value in cnf_grammer.items():
					#print([length-p,s,length-l+p,s+p]).       #print matrix index
					if mat[length-p][s] and mat[length-l+p][s+p]:
						for first_pt in mat[length-p][s]:
							for second_pt in mat[length-l+p][s+p]:
								for rule in value:
									# print('test',first_pt+' '+second_pt)
									# print('rule',rule)
									if first_pt+' '+second_pt == rule:
										print(rule)
										mat[length-l][s].append(key)
										print_mat(mat)
#       for each production Ra -> Rb Rc
				# for key, value in cnf_grammer.items():
				# 	if(mat[s+1][s])
	if mat[0][0]:
		return 1,length, mat
	
	else:
		return 0,length, mat

#         if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
# if P[n,1,1] is true then
#   I is member of language
# else
#   I is not member of language
	#return result and process

def print_mat(mat):
	[print(line) for line in mat]
def print_dict(this_dict):
	for key,val in this_dict.items():
		print(key,val)

if __name__ == '__main__':
	file_name = "short_grammer_1.txt"
	grammer = import_grammer_from_file(file_name)
	cnf_grammer = CFG_to_CNF(grammer)
	print_dict(cnf_grammer)
	sentence='the duck duck a cat'
	parse_success, length, mat = CKY_parse(sentence,cnf_grammer)
	print ('This program is being run by itself')

	fig = plt.figure(0)
	ax=fig.add_subplot(111)
	ax.axis([0, length, 0,length])
	ax.grid(color='r', linestyle='-', linewidth=1)
	split_sen = sentence.split()
	for i in range(length):
		ax.text(i+0.5, -0.3, split_sen[i])
	for i in range(length):
		for j in range(length):
			if mat[i][j]:
				ax.text(j+0.4, length-i-0.5, mat[i][j])

	x=length-0.05
	y=length-0.15
	for key, value in grammer.items():
		line = str(key) + str(value)
		ax.text(x,y, line,fontsize=10,horizontalalignment='right')
		y-=.2
		
	plt.show()


else:
	print ('I am being imported from another module')













