import requests
import os
from bs4 import BeautifulSoup
class GithubDownload():
    def __init__(self):
        pass
    
    def get_html(self,url):
        result=requests.get(url)
        if(result.status_code==200):
            html_content = BeautifulSoup(result.content, "html.parser")
        return html_content

    def get_tile(self,html_content):
        label_latest=html_content.find_all(class_="label-latest")[0]
        release_title=label_latest.find_all(class_="release-title")[0]
        release_title=release_title.a.text
        return release_title

    def get_code(self,html_content):
        label_latest=html_content.find_all(class_="label-latest")[0]
        release_downloads=label_latest.find_all(class_="release-downloads")[0]
        release_zip=release_downloads.li.a['href']
        return release_zip

    def get_time(self,html_content):
        label_latest = html_content.find_all(class_="label-latest")[0]
        release_authorship = label_latest.find_all(class_="release-authorship")[0]
        release_version = release_authorship
        release_time=release_version.a.next_sibling.next_sibling.text
        return release_time

    def get_version(self,html_content):
        label_latest=html_content.find_all(class_="label-latest")[0]
        css_truncate_target=label_latest.find_all(class_="css-truncate-target")[0]
        release_version=css_truncate_target.text
        return release_version

    def get_dir(self,name,version):
        print os.path.exists(name)
        cwd = os.getcwd()
        print cwd
        file_dir = os.path.join(cwd, name)
        print file_dir
        zip_name = version + ".zip"
        zip_dir = os.path.join(file_dir, zip_name)
        return zip_dir

