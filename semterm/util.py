import os

def execute_with_terminal(cmd):
	os.system('''
		terminator --geometry=+100+100 -e "echo semterm call: {cmd}; {cmd}; 
		sleep 1.5" &'''.format(cmd=cmd))