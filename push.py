#!/usr/bin/env python
import subprocess
import os 


def cmd(cmd):
	os.system(cmd)

cmd('clear')
print 'Updating...'
comment = raw_input("Type git-commit comment: ")				
cmd('git add *')			
cmd('git status')
cmd('git diff')
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
cmd('echo "\e[0;31mPush Script Complete!"')