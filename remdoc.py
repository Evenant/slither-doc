import docgen_config as cfg
import os
from genericpath import isfile,isdir

def get_files(path = "")->list[str]:
	if path.startswith("./"):
		path = path[1:]
		path = path[1:]
	if path == "":
		path = "."
	elif path in cfg.GEN_IGNORE_DIRS:
		return []
	
	# Returns an empty list if it finds out that this directory is not allowed
	if path in cfg.GEN_IGNORE_DIRS:
		return []

	listed = os.listdir(path.split("/")[-1])
	files:list[str] = []

	os.chdir(path.split("/")[-1])
	# is it a file or directory?
	for f_or_d in listed:
		if isfile(f_or_d):
			if f_or_d.endswith(("html","md")) and f_or_d.startswith("README") == False:
				os.remove(f_or_d)

		if isdir(f_or_d):
			nextdir = get_files(path + "/"+ f_or_d)
			for f in nextdir:
				files.append(f)
	if path != ".":
		os.chdir("..")
	return files

get_files()