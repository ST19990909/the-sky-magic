import sys
import urllib.request
import re
import os
import threading
import time
import requests

BASE_URL = 'https://mypages.valdosta.edu/rpmihail/skyfinder/images/'
BASE_MASK_URL='https://mypages.valdosta.edu/rpmihail/skyfinder/'
ZIP_LINK = '&nbsp;<a href="(.*)">'
MASK_LINK="<a href='(.*)'>"

DataTempDir = "dataTemp"


# print(doc)

if os.path.exists(DataTempDir) is False:
    os.mkdir(DataTempDir)
    os.mkdir(DataTempDir+'/Masks')


def report(count, blockSize, totalSize):

  percent = int(count*blockSize*100/totalSize)

  sys.stdout.write("\r%d%%" % percent + ' complete')

  sys.stdout.flush()

if __name__ == '__main__':
    req = urllib.request.Request(BASE_URL + "index.html")
    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')
    url_list = list(set(re.findall(ZIP_LINK, doc)))
    mask_list=list(set(re.findall(MASK_LINK,doc)))
    for file in url_list:
        if os.path.exists(DataTempDir + "/" + file[2:]) is False:
            print(file[2:] + " begin ")
            urllib.request.urlretrieve(BASE_URL+file[2:], DataTempDir + "/" + file[2:],reporthook=report)
            sys.stdout.write("\rDownload complete, saved as "+ (file[2:]) + '\n')
            sys.stdout.flush()
        else:
            continue;
    print("all file downoad!")

    for mask in mask_list:
        if os.path.exists(DataTempDir + "/Masks/" + mask[9:]) is False:
            print(mask[2:] + " begin ")
            urllib.request.urlretrieve(BASE_MASK_URL + mask[3:], DataTempDir + "/Masks/" + mask[9:], reporthook=report)
            sys.stdout.write("\rDownload complete, saved as " + (mask[9:]) + '\n')
            sys.stdout.flush()
        else:
            continue;
            #https://mypages.valdosta.edu/rpmihail/skyfinder/images/11160.zip
            #https://mypages.valdosta.edu/rpmihail/skyfinder/Masks/10870.png
    print("all mask downoad!")
    #print(file[2:]+" over")

    # for file in url_list:
    #     if os.path.exists(DataTempDir + "/" + file[2:]) is False:
    #         t = download(BASE_URL + file[2:], DataTempDir + "/" + file[2:])
    #         while t.is_alive():
    #             time.sleep(60)
    #         print("bye")
    #     else:
    #         continue;
    #print("all file downoad!")
