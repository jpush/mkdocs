import commands
import os
print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/jpush/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/jmessage/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/jsms/"))
print (commands.getstatusoutput("mkdocs build --clean"))

