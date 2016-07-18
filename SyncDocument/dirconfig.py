import os
#config the dir of the mkdocs docs dir
conf={}

conf["mkdocs"]=os.getcwd()
jiguang_docs=os.path.join(conf["mkdocs"],"jiguang-docs")
conf["jiguang_docs"]=jiguang_docs

conf["zip"]=os.path.join(conf["mkdocs"],"download-zip")

#jpush dir
conf["jpush_dir"]=os.path.join(conf["jiguang_docs"],"jpush")
conf["jpush_docs"]=os.path.join(conf["jpush_dir"],"docs")
#conf["jmessage"]=os.path.join(conf["jiguang_docs"],"jmessage")

conf["jpush"]={}

#jpush -> server dir
conf["server"]=os.path.join(conf["jpush_docs"],"server")
conf["jpush"]["server"]={}
conf["jpush"]["server"]["jpush-api-csharp-client"]=os.path.join(conf["server"],"csharp_sdk.md")
conf["jpush"]["server"]["jpush-api-python-client"]=os.path.join(conf["server"],"python_sdk.md")

