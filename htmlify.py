from genericpath import isdir, isfile
import markdown2
import docgen_config as cfg
import os

cssf = open("style.css")
css_text = cssf.read()
cssf.close()

def convert_to_html(mdfilepath:str) -> str:
	mdf = open(mdfilepath)
	hfpath = mdfilepath[:-3] + ".html"
	hf = open(hfpath, "wt")

	hf.write(f"<style>{css_text}</style>")
	hf.write(markdown2.markdown(mdf.read().replace(".md",".html")).replace("\n","<br/>"))

	hf.close()
	mdf.close()
	return hfpath
# A recursive function that returns a list of file paths
def get_files(path = "")->list[str]:
	if path.startswith("./"):
		path = path[1:]
		path = path[1:]
	if path == "":
		path = "."
	
	# Returns an empty list if it finds out that this directory is not allowed
	if path in cfg.GEN_IGNORE_DIRS:
		return []

	listed = os.listdir(path.split("/")[-1])
	files:list[str] = []

	os.chdir(path.split("/")[-1])
	# is it a file or directory?
	for f_or_d in listed:
		if isfile(f_or_d):
			if f_or_d.endswith(".md"):
				files.append(f"{path}/{f_or_d}")
		if isdir(f_or_d):
			nextdir = get_files(path + "/"+ f_or_d)
			for f in nextdir:
				files.append(f)
	if path != ".":
		os.chdir("..")

	return files
for x in get_files():
	hfpath = convert_to_html(x)
	if cfg.HTML_DIR != "":
		dirpath = hfpath
		while dirpath[-1] != "/":
			dirpath = dirpath[:-1]
		dirpath = dirpath[:-1]
		dirpath = cfg.HTML_DIR +"/"+ dirpath
		if not os.path.exists(dirpath):
			os.makedirs(dirpath)
		old_hf = open(hfpath)
		new_hf =open(cfg.HTML_DIR +"/"+ hfpath,"wt")
		new_hf.write(old_hf.read())
		old_hf.close()
		new_hf.close()
		os.remove(hfpath)