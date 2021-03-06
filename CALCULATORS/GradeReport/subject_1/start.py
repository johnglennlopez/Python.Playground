#!/usr/bin/env python
from data_lib import *		# Database
from main import *
import subprocess			# Subprocess for Shell CMD
import os 					# OS Library


'''
This is the start-up/output sequence for computing numbers from 
the txt Database
'''


# COLOR LIBRARY
class colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# CMD FUNCTION - for running shell scripts 
def cmd(cmd):
	os.system(cmd)

#CALCULATIONS
avg_subj_1 = get_average(subj_1)
avg_hmw = average(subj_1['homework'])
avg_qzz = average(subj_1['quizzes'])
avg_tst = average(subj_1['tests'])

p_hmw = hmw_wght*100		# Current weight for homework
p_qz = qzz_wght*100			# Current weight for quiz
p_tst = tst_wght*100		# Current weight for test

#OUTPUTS
#cmd('clear') #<--- ONLY HAVE THIS IF SINGLE
print colors.BOLD + "Homework Average: " + colors.WHITE + "%s (worth %s%%)" %(avg_hmw, p_hmw)
print colors.BOLD + "Quiz Average: " + colors.WHITE + "%s (worth %s%%)" %(avg_qzz, p_qz)
print colors.BOLD + "Test Average: " + colors.WHITE + "%s (worth %s%%)" %(avg_tst, p_tst)
print

if avg_subj_1 <= 60:
	print "Your Total for this subject so far is " + colors.RED + "%s%%" %(avg_subj_1)

elif avg_subj_1 <= 79:
	print "Your Total for this subject so far is " + colors.YELLOW + "%s%%" %(avg_subj_1)

else:
	print "Your Total for this subject so far is " + colors.GREEN + "%s%%" %(avg_subj_1)

#OUTPUT TO FILE
#cmd('python start.py > out.txt')