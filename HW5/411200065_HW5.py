import os
os.getcwd()
file=open("411200065_趙宇森.txt","w")
print("系級:{}\n學號:{}\n姓名:{}".format("數資統一","411200065","趙宇森"),file=file,end="")
file.close()
file1=open("all student.txt","a")
print("{}_{}".format("411200065","趙宇森"),file=file1,end="\n")
file1.close()
