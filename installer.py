import requests
import tarfile
import zipfile
import platform
import os

def make_username():
    return os.path.expanduser('~')

def downloadMac(packageNumber, installPath):
    url = 'https://github.com/LunarJack/Project-Epsilon/archive/refs/heads/main.zip'
    response = requests.get(url)
    try:
        os.mkdir(".TMP")
    except FileExistsError:
        pass
    file_Path = '.TMP/main.zip'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            file.close()
        print('\nFile downloaded successfully')
    else:
        print('\nFailed to download file')
    try:
        os.mkdir(installPath)
    except FileExistsError:
        pass
    with zipfile.ZipFile('.TMP/main.zip', 'r') as zip:
        zip.extractall(installPath)
        print('File unzipped successfully')

print("Welcome to the Project epsilon installer!\nWhat would you like to install?\n\n1: The main package.\n\nType in the number of what you want:")
package = input()
installPath = input("\nWere would you like to install it? (Default: ~/Epsilon, Unix; /Epsilon, Windows)\n")
platform = platform.system()
if platform == 'Darwin':
    if installPath == '':
        installPath = make_username()
    downloadMac(package, installPath)
elif platform == 'Windows':
    if installPath == '':
        installPath = '/Epsilon'
    exit()