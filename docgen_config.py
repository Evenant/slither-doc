# This file is for configuring how this generator works

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
	".obsidian"
}

# File extensions to ignore
# Pretty self explanatory
# You can also have files to be ignored here
GEN_EXT_IGNORE = (
	"gitignore",
	"md", # Make sure that the documentation generator does not document documentation
	"bat"
)