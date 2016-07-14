#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
import zipfile
import urllib

from githubdownload import GithubDownload
from repositories import repositories
from ziptool import ZipTool

downloader=GithubDownload()
for file_dic in repositories:
     html_content = downloader.get_html(repositories[file_dic]["url"]+"/releases")
     title = downloader.get_tile(html_content)
     zip_url = downloader.get_code(html_content)
     release_time = downloader.get_time(html_content)
     release_version = downloader.get_version(html_content)

     if(not os.path.exists(repositories[file_dic]["name"])):
          os.mkdir(repositories[file_dic]["name"])
     zip_dir=downloader.get_dir(name=repositories[file_dic]["name"],version=release_version)
     zip_tool=ZipTool()
     zip_tool.zip_download(zip_dir,release_version,repositories[file_dic]["url"])
     zip_tool.unzip_file(repositories[file_dic]["name"],release_version)