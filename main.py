import os

# Make the folder if not exists
def makeFolder(floder):
    if not os.path.exists(floder):
        os.makedirs(floder)

# Move the files to there folder
def move(foldName, files):
    for file in files:
        os.replace(file, f"{foldName}/{file}")

files = os.listdir()
files.remove("main.py") # Remove the file 'main.py' file so it will not move

# Making the folders
makeFolder("Images")
makeFolder("Media")
makeFolder("Docs")
makeFolder("Other")

# Choosing the files that will be moved to folders
imgExts = ['.png', '.jpeg', '.jpg']
img = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = ['.docx', '.txt', '.logs', '.doc', '.pdf']
doc = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

medExts = ['.mp3', '.mp4', '.wav']
med = [file for file in files if os.path.splitext(file)[1].lower() in medExts]

oth = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (not ext in medExts) and (not ext in docExts) and (not ext in imgExts) and (not os.path.isdir(file)):
        oth.append(file)

# Moving the files
move("Docs", doc)
move("Images", img)
move("Media", med)
move("Other", oth)
