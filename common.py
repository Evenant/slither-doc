import docgen_config as cfg
from genericpath import isdir,isfile
import os

class files_and_dirs:
	files:list[str] = []
	directories:list[str] = []
	def search(self,ignoredirs:set[str],path = "")->list[str]:
		if path.startswith("./"):
			path = path[1:]
			path = path[1:]
		if path == "":
			path = "."		
		# Returns an empty list if it finds out that this directory is not allowed
		if path in ignoredirs:
			return []

		listed = os.listdir(path.split("/")[-1])
		files:list[str] = []

		os.chdir(path.split("/")[-1])
		# is it a file or directory?
		for f_or_d in listed:
			if isfile(f_or_d):
				self.files.append(path + "/" + f_or_d)

			if isdir(f_or_d):
				nextdir = self.search(ignoredirs,path + "/"+ f_or_d)
				for f in nextdir:
					files.append(f)
		if path != ".":
			os.chdir("..")
		return files
	def get_files(self) -> list[str]:
		return self.files
	def get_dirs(self) -> list[str]:
		return self.directories

	def exclude_files_with_filter(self,filter:tuple) -> list[str]:
		temp:list[str] = []
		for i in self.files:
			if not i.endswith(filter):
				temp.append(i)
		return temp
	def include_files_with_filter(self,filter:tuple)-> list[str]:
		temp:list[str]= []
		for i in self.files:
			if i.endswith(filter):
				temp.append(i)
		return temp
	def __init__(self,ignoredirs:set[str]) -> None:
		self.search(ignoredirs)