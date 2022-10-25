# This file is for configuring how this generator works
# See the bottom of this file to learn how to configure and use SlitherDoc

# If you disagree with SlitherDocs "document on the spot" philosophy
# you can set dedicated directories for markdown and html files to be in.
# The file strucure of your project will still be replicated in the dedicated dirs.
MARKDOWN_DIR = ""
HTML_DIR = ""

# A dictionary full of file extensions with their appropriate comment types
# Slash comments are "slash" or "/"
# Hash comments are "hash" or "#"
# Dash comments are "dash" or "-"
GEN_EXT = [
	("cpp","slash"),
	("c","slash"),
	("cs","slash"),
	("lua","-"),
	("py","#"),
	("h","/")
]

# Tells this generator which directories to ignore
GEN_IGNORE_DIRS = {
	".git",
	"lookan-py",
	".vscode",
	"__pycache__",
	".obsidian",
	"docs"
}

# File extensions to ignore
# Pretty self explanatory
# You can also have files to be ignored here
GEN_EXT_IGNORE = (
	"gitignore",
	"md", # Make sure that the documentation generator does not document documentation
	"bat",
	"html",
	"css",
	"markdown2.py", # You can also make the generator ignore filenames, but this is not recommended
	"docgen.py",
	"docgen_config.py",
	"htmlify.py"
)
"""
SlitherDoc User Manual

First, configure how the generator should act towards different file extensions.
GEN_EXT = [
	('py','#'),
	('c','/'),
	('lua','dash')
]
The above will make the generator search for:
'###' comments in .py files
'///' comments in .c files
'---' comments in .lua files

There might be some directories that you want the generator to ignore, like an already
documented dependency of the project or binary/library directories.
GEN_IGNORE_DIRS = {
	'.git',
	'bin',
	'lib',
	'deps/extlib'
}
The above will make the generator ignore .git, bin and lib directories, and it will also tell the 
generator to ignore deps/extlib, but not to ignore deps

There is always gonna be filetypes that never need to be documented, like executables, plain text
and even Markdown files.
GEN_EXT_IGNORE = (
	'md', # Always make usre you have this
	'html',
	'exe',
	'bat',
	'sh',
	'dll',
	'lib',
	'gitignore',
	'txt'
)
The above is self-explanatory

Now run `python docgen.py` and watch as each file gets its own .md file and each directory gets its own Index.md file.
After it is finished, you can generate a static html site using `python htmlify.py` to convert the markdown into html.

It is recommended you create a .gitignore file and paste the following into the file:
*.md
*.html
!README.md
!README.html

The above will ignore any markdown and html files in your project but keep the README's in.
If your project is based on web development and you NEED the html, add an exception directory
that contains the html files your website needs:
!my_website/*.html

The above will NOT ignore the html files in the 'my_website' directory.
Make sure that GEN_IGNORE_DIRS has a "my_website" value aswell

Your project structure doubles as a documentation site, all that the users of your software
need to do in order to view the project documentation is run 'python docgen.py', no need for a
dedicated docs directory.

If you DO want a dedicated docs directory for markdown and html, do the following steps:
- Go to the top of this file and set MARKDOWN_DIR to ""
- Set HTML_DIR to "docs/html"
- Run `python docgen.py`
- Run `python htmlify.py`
- Set MARKDOWN_DIR to "docs/markdown"
- Run `python docgen.py`
Do the above and you will have a docs directory containing the documentation for your project

If you would like to clean up the documentation junk from your project, run `python remdoc.py`
It will remove every single .html and .md file it can access but ignores README's.
"""
