import os

dirName = 'C:\Users\some\directory'

def directory_access(folderDirectory):
    for path, subdirs, files in os.walk(folderDirectory):
       for fileItems in files:     
         print fileItems

directory_access(dirName)
