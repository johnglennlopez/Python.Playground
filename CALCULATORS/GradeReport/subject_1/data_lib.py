#!/usr/bin/env python

'''
This converts textfiles into a workable database list. 
Do not change anything unless you are adding a new library.
'''

# TESTS LIBRARY
tests = []
with open('subject_1/test.txt') as inputfile:
	for nums in inputfile:
		tests.append(nums)
tests = map(int, nums.split(","))

# QUIZZES LIBRARY
quizzes = []
with open('subject_1/quizzes.txt') as inputfile:
	for nums in inputfile:
		quizzes.append(nums)
quizzes = map(int, nums.split(","))

# HOMEWORK LIBRARY
homework = []
with open('subject_1/homework.txt') as inputfile:
	for nums in inputfile:
		homework.append(nums)
homework = map(int, nums.split(","))




######### 
subj_1 = {
'tests' : tests, 'quizzes' : quizzes, 'homework' : homework
}
