import os
os.getcwd()
file=open("輸出結果.txt","w")
number=eval(input("輸入一個數:"))
size=input("請輸入物品尺寸:")
color=input("請輸入物品顏色:")
if (number%2)==0:
    print(f"{number}是偶數",file=file)
elif (number%2)==1:
    print(f"{number}是奇數",file=file)
else:
    print(f"{number}為非整數",file=file)
if size=="小" and color=="白":
    print("尺寸為小且顏色為白的是白米",file=file)
elif size=="大" and color=="白":
    print("尺寸為大且顏色為白的是雲朵",file=file)
elif size=="小" and color=="黑":
    print("尺寸為小且顏色為黑的是芝麻",file=file)
else:
    print("無法判斷物品",file=file)
file.close()