import requests
import os
import zipfile
from githubdownload import GithubDownload
from repositories import repositories
import dirconfig
import shutil

class ZipTool():
    def zip_download(self,zip_dir,release_version,url):
        with open(zip_dir, "wb") as code:
            download_url = url + "/archive/" + release_version + ".zip"
            download_response = requests.get(download_url)
            code.write(download_response.content)

    def unzip_file(self,name,release_version):
        filename = os.path.join(dirconfig.conf["zip"], name)
        filename = os.path.join(filename, release_version+".zip")
        print (filename)
        filedir = os.path.join(dirconfig.conf["zip"], name)
        filedir = os.path.join(filedir, 'data/')

        fz = zipfile.ZipFile(filename)
        if fz:
            fz = zipfile.ZipFile(filename, 'r')
            for file in fz.namelist():
                fz.extract(file, filedir)
        else:
            print('This file is not zip file')


    def replace_readme(self,name,release_version):
        file_dir = os.path.join(dirconfig.conf["zip"], name)
        file_dir = os.path.join(file_dir, 'data')
        release_dir=name+"-"+release_version[1:]
        file_dir=os.path.join(file_dir, release_dir)
        file_dir=os.path.join(file_dir, "README.md")
        print file_dir
        readme_dir=dirconfig.conf["jpush"]["server"][name]
        print readme_dir
        print shutil.copyfile(file_dir,readme_dir)































