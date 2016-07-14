import requests
import os
import zipfile
from githubdownload import GithubDownload
from repositories import repositories

class ZipTool():
    def zip_download(self,zip_dir,release_version,url):
        with open(zip_dir, "wb") as code:
            download_url = url + "/archive/" + release_version + ".zip"
            download_response = requests.get(download_url)
            code.write(download_response.content)

    def unzip_file(self,name,release_version):
        cwd = os.getcwd()
        filename = os.path.join(cwd, name)
        filename = os.path.join(filename, release_version+".zip")
        print (filename)
        '''
        if (not os.path.exists("data")):
            os.mkdir("data")
        '''
        filedir = os.path.join(cwd, name)
        filedir = os.path.join(filedir, 'data/')

        fz = zipfile.ZipFile(filename)
        if fz:
            fz = zipfile.ZipFile(filename, 'r')
            for file in fz.namelist():
                fz.extract(file, filedir)
        else:
            print('This file is not zip file')




