import re
import sys


file_1 = open(sys.argv[1], 'r') # accept revision
file_2 = open(sys.argv[2], 'r') # provide the x, y, z coordinates of LYR that has been twisted with specific angles

file_1_list = file_1.readlines()
file_2_list = file_2.readlines()

# modification with re
j = 0 
for i in file_1_list: 
	pattern = re.compile(r'ALYR.*[A-Z]$') 
	n = pattern.findall(i) 
	if len(n) != 0: 
		sub = re.sub(r'(-?(\ \d|\d+)\.[0-9]{3}\ +){2}-?\ ?\d+\.[0-9]{3}', str(file_2_list[j].replace('\n', '')), str(i)).replace('\n', '')
		print(sub) # output
		j += 1
		
