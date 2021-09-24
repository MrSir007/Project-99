import time
import os
import shutil

def main () :
  deletedfolders = 0
  deletedfiles = 0
  path = "/path_to_delete"
  days = 30
  seconds = time.time(days*24*60^2)

  if os.path.exists(path) :
    for rootfolder,folders,files in os.walk(path) :
      if seconds>=get_file_or_folder_age(rootfolder) :
        remove_folder(rootfolder)
        deletedfolders += 1
        break
      else :
        for eachfolder in folders :
          folderpath = ospath.join(rootfolder,eachfolder)
          if seconds>=get_file_or_folder_age(folderpath) :
            remove_folder(folderpath)
            deletedfolders += 1
            break
        for eachfile in files :
          filepath = ospath.join(rootfolder,eachfile)
          if seconds>=get_file_or_folder_age(filepath) :
            remove_folder(filepath)
            deletedfiles += 1
            break
