#!/usr/bin/env python
import subprocess
import os 


def cmd(cmd):
	os.system(cmd)

comment = raw_input("Type Comment: ")
cmd('clear')				
cmd('git add *')			
cmd('git status')
cmd('git diff')
cmd("git commit -m '"+comment+"'")
cmd('git push')
print 
cmd('\e[0;31mecho Push Script Complete!\e[0m')