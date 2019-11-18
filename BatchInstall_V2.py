#BatchInstall_V2.py
import os
'''libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}
libs=list(libs)
print(libs)
textWritein=open("BatchInstall.txt",'wt')
for lib in libs[:-1:1]:
    textWritein.write(lib+'\n')
textWritein.write(libs[-1])
textWritein.close()'''
fileName=input("请输入要打开的txt文件（pip安装文件，放于同目录下）：")
fileHandle=open(fileName,"rt")
try:
    for line in fileHandle.readlines():
        os.system('pip3 install '+line)
except:
    print("Failed Somehow")
fileHandle.close()
os.system("pause")

