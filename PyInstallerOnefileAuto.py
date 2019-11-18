#PyInstallerOnefileAuto.py
import os
import shutil
fileName=input("请输入要打包为可执行文件的.py文件（放于同目录下）：")
try:
    os.system('pyinstaller -F --clean '+fileName)
    print("Succeed.")
except:
    print("Failed Somehow.")
fileName=fileName[:-3]
'''
print(os.getcwd())
print(os.path.abspath('.')) #获取当前工作目录路径
print(os.path.abspath('test.txt') )#获取当前目录文件下的工作目录路径
print(os.path.abspath('..')) #获取当前工作的父目录 ！注意是父目录路径
print(os.path.abspath(os.curdir)) #获取当前工作目录路径
'''
filePath=os.path.abspath('.')
os.remove(fileName+'.spec')
shutil.copyfile(os.path.abspath('.')+'\\dist\\'+fileName+'.exe',\
                os.path.abspath('.')+'\\'+fileName+'.exe')
#os.system('copy .\\dist\\'+fileName+'.exe .\\')
shutil.rmtree(filePath+'\\__pycache__')
shutil.rmtree(filePath+'\\build')
shutil.rmtree(filePath+'\\dist')
'''非空目录会报错
os.removedirs(filePath+'\\__pycache__')
os.removedirs(filePath+'\\build')
os.removedirs(filePath+'\\dist')
#os.system("rd /s .\\__pycache__")
#os.system("rd /s .\\build")
#os.system("rd /s .\\dist")
'''
os.system("pause")

