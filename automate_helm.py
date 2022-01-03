import os

root_path = './'

folders = ['api01_back', 'api02_front', 'api03', 'api04']

gh = foldersprint(gh)

for folder in gh:
  os.system("/snap/bin/helm create " + folder)

