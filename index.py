import git
from sys import argv
import os
from colorama import *
init(autoreset=True)

try:
    url = argv[1]
except:
    print(Fore.WHITE + Back.RED + 'This program need an url!')
    url=input("Please enter an url:")

try:
    folder = argv[2]
except:
    print(Fore.WHITE + Back.RED + 'This program need a Foldername!')
    folder=input("Please enter a Foldername:")

if os.path.isdir(folder):
	if len(os.listdir(folder)) == 0:
		print("Start cloning from "+url+" in "+folder)

		try:
			git.Repo.clone_from(url, folder)
		except Exception as e:
			print(Fore.WHITE + Back.RED+"ERROR: "+str(e))
			exit()
		
		print("Cloning succesful in "+folder+" from "+url)
	else: 
		print(Fore.WHITE + Back.RED + 'The folder '+folder+" is not empty.")
else:
	print(Fore.WHITE + Back.RED + 'The folder '+folder+" does not exist.")