#/usr/bin/python

import os

# Define kind of slash ('\' for Windows systems and '/' for Linux/Unix/MacOS systems)

if os.name == 'nt':
	slash = '\\'
else:
	slash = '/'

# Recursive delete function

def del_file(directory, filename):
	
	# Lists the elements of the given directory
	
	dirs = os.listdir(directory)
	
	for file in dirs:
		
		# If the element is a subdirectory the delete function is loaded with that directory
		
		if  os.path.isdir(directory + slash +  file):
			del_file(directory + slash + file)
		
		# If the element is the searched file it will be deleted
		
		elif file == filename:
			print('Deleting ' + directory + filename)
			os.remove(directory + filename)

# Function to define the file and the root directory to delete recursively

def remove_file_recursively():
	
	# Name of the files to delete
	
	#filename = ''
	filename = input("Give the file's name to delete: ")
	
	# Check if the file contains any slash symbol, only files can be deleted, not directories
	
	if slash in filename:
		print("Error: file name can't have \"" + slash + "\" symbol")
		exit()
	
	# Root directory where the files will be deleted
	
	#root_dir = ''
	root_dir = input("Give the root directory to delete the given file: ")
	
	# Check if the directory exists and it is not a file
	
	if os.path.isdir(root_dir):
		if os.path.isfile(root_dir):
			print("Error: the given directory is a file")
			exit()
		else:
			print("Error: the directory does not exist")
	
	# If the root directory has no slash it is added
	
	if root_dir[len(root_dir)-1] != slash:
		directory = root_dir + slash
	else:
		directory = root_dir
	
	# The function to delete files is loaded
	
	del_file(directory, filename)

remove_file_recursively()
