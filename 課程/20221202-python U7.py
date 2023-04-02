# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:31:37 2022

@author: Administrator
"""


# ch7_1.py
sum = 1+2+3+4+5+6+7+8+9+10
print("總和 = ", sum)

'''
# ch7_2.py -- 不完整的程式
vipNames = ['James','Linda','Peter', ... , 'Kevin']
print("客戶1 = ", vipNames[0])
print("客戶2 = ", vipNames[1])
print("客戶3 = ", vipNames[2])
...
...
print("客戶1000 = ", vipNames[999])
'''

''' for 迴圈 '''
'''
for 變數in 物件:
    程式碼區塊

(物件為可跌代物件：串列、元組、字典、集合 與 range<生產器>)
'''

# ch7_3.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:
    print(player)

# ch7_4.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:print(player)

# ch7_5.py
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(f"{player.title()}, it was a great game.")
    print(f"我迫不及待想看下一場比賽 {player.title()}")

# ch7_6.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)

# ch7_7.py
files = ['da1.c','da2.py','da3.py','da4.java']
py = []
for file in files:
    if file.endswith('.py'):    # 以.py為副檔名
        py.append(file)         # 加入串列
print(py)

'''　range 生產器
range(start,stop,step)

'''

print(range(5))
print(list(range(5)))

list(range(5,10))
list(range(5,10,2))
list(range(5,10,3))
list(range(10,5,-1))


for i in range(5):print(i)
a=range(5)
alist=list(a)
for i in a:print(i)
for i in alist:print(i)



#如何製作自己的生產器(日後有機會說)

# ch7_8.py
n = int(input("請輸入星號數量 : ")) # 定義星號的數量                           
for number in range(n):             # for迴圈    
    print("*",end="")               # 列印星號

# ch7_9.py
money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print(f"第 {i+1} 年本金和 : {int(money)}")

# ch7_10.py
n = int(input("請輸入n值 : "))
sum = 0
for num in range(1,n+1):
    sum += num
print("總和 = ", sum)

# ch7_11.py
n = int(input("請輸入整數:"))
total = sum(range(n + 1))
print(f"從1到{n}的總和是 = {total}")

# ch7_12.py
squares = []                     # 建立空串列
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    squares.append(num ** 2)     # 加入串列
print(squares)

# ch7_13.py
xlst = []
xlst.append(0)
xlst.append(1)
xlst.append(2)
xlst.append(3)
xlst.append(4)
xlst.append(5)
print(xlst)

# ch7_14.py
xlst = []
for n in range(6):
    xlst.append(n)
print(xlst)

# ch7_15.py
xlst = list(range(6))
print(xlst)

# ch7_16.py(很常用)
xlst = [ n for n in range(6)]
print(xlst)

# ch7_17.py
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
squares = [num ** 2 for num in range(1, n+1)]
print(squares)

#相依變數跌代
# ch7_18.py 
x = [[a, b, c] for a in range(1,20) for b in range(a,20) for c in range(b,20)
     if a ** 2 + b ** 2 == c **2]
print(x)

#7-2-8
for x in range(1,128):
    print(chr(x),end="")


for x in range(0x6d2a,0x6e2a):
    print(chr(x),end="")


'''巢狀迴圈'''

print("◣")
for i in range(1, 10):
    for j in range(1, 10):
            if j<=i:
                print("▇",end="")
            if j==i:
                print("◣",end="")
    print ()
#####################################
'''break 跳出(終止)當前迴圈'''
print("◣")
for i in range(1, 10):
    for j in range(1, 10):
            if j<=i:
                print("▇",end="")
            if j==i:
                break
    print ()

####################################
print("◣")
for i in range(1, 10):
    for j in range(1, 10):
            if j<=i:
                print("▇",end="")
            if j==i:
                print("◣",end="")
    break
    print ()

# ch7_19.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
    print()         # 換列輸出

# ch7_20.py
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("aa", end="")
    print()                # 換列輸出

'''break 跳出(終止)迴圈 '''
# ch7_21.py
players = ['Curry','Jordan','James','Durant','Obama','Kevin','Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1                          # 索引加1


# ch7_22.py
scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)         # 從大到小排列
count = 0
for sc in scores:
    count += 1
    print(sc, end=" ")
    if count == 5:                  # 取前5名成績
        break                       # 離開for迴圈

'''continue 跳下一圈(忽略當前迴圈後方所有執行)'''

for i in range(1, 10):
    if(i ==3):
        continue
    print(i)
    

# ch7_23.py
scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:                  # 小於30則不往下執行
        continue
    games += 1                      # 場次加1              
print(f"有{games}場得分超過30分")

# ch7_24.py
players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
for player in players:
    if player[1] < 200:
        continue
    print(player)

# ch7_25.py
num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:                            # 2是質數所以直接輸出
    print(f"{num}是質數")
else:
    for n in range(2, num):             # 用2 .. num-1當除數測試
        if num % n == 0:                # 如果整除則不是質數
            print(f"{num}不是質數")
            break                       # 離開迴圈
    else:                               # 否則是質數
        print(f"{num}是質數")

#印出有限個質數
num = int(input("請輸入大於1的整數做質數測試 = "))
y=[]
for i in range(2,num+1):
    if(all([t!=0 for t in [i%x for x in range(2,int(i/2)+1)]])):
        y.append(i)

print(y)


'''  while  迴圈 '''#有些程式語言 語法為 repeat
'''
while 執行條件:
    程式碼區塊
'''
a=1
while a<5:
    print(a)
    a=a+1
    
'''例子：漸進取值'''
#找 2開方值 (使用取平方的二分法)
#誤差條件
e=10e-8
a=1
b=2
n=0
while b-a > e :
    c=a+(b-a)/2
    disc=c**2-2
    if disc>0:
        b=c
    else:
        a=c
    n=n+1

print(c)


#跳出迴圈(次數上條件)

e=10e-20
a=1
b=2
n=0
while b-a > e :
    if n > 1e5:
        break
    c=a+(b-a)/2
    disc=c**2-2
    if disc>0:
        b=c
    else:
        a=c
    n=n+1
print(c)
print(n)

#或是直接加在執行條件
e=10e-20
a=1
b=2
n=0
while b-a > e and n <1e5:
    c=a+(b-a)/2
    disc=c**2-2
    if disc>0:
        b=c
    else:
        a=c
    n=n+1

#甚至回傳停止迴圈的條件
e=10e-20
a=1
b=2
n=0
keeprun=True
while keeprun: 
    c=a+(b-a)/2
    disc=c**2-2
    if disc>0:
        b=c
    else:
        a=c
    n=n+1
    if b-a < e :
        keeprun=False
        print("達到前後誤差條件")
    elif n > 1e5:
        keeprun=False
        print("達到最大計算次數")
print(c)

#簡短程式碼(不是重點)
e=10e-20
a=1
b=2
n=0
keeprun=True
while keeprun: 
    c=a+(b-a)/2
    disc=c**2-2
    if disc>0:
        b=c
    else:
        a=c
    n=n+1
    keeprun =  b-a > e and n < 1e5
    if not keeprun:
        print("達到前後誤差條件" * (b-a < e) + \
            "達到最大計算次數" * (n > 1e5-1))

print(c)

# ch7_26.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
input_msg = ''                  # 預設為空字串
while input_msg != 'q':
    input_msg = input(msg)
    if input_msg != 'q':        # 如果輸入不是q才輸出訊息         
        print(input_msg)


# ch7_27.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
active = True
while active:               # 迴圈進行直到active是False
    input_msg = input(msg)
    if input_msg != 'q':    # 如果輸入不是q才輸出訊息         
        print(input_msg)
    else:
        active = False      # 輸入是q所以將active設為False

# ch7_28.py
n = int(input("請輸入一個值 : "))
sum = 0
while n:
    sum += n
    n = int(input("請輸入一個值 : "))
print("輸入總和 = ", sum)

'''巢狀設計'''

# ch7_29.py
i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換列輸出
    i += 1              # 外層迴圈加1

'''break 與 continue 使用方式與for 迴圈相同'''
# ch7_30.py
msg1 = '人機對話專欄,請告訴我妳喜歡吃的水果!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
while True:                     # 這是while無限迴圈
    input_msg = input(msg)
    if input_msg == 'q':        # 輸入q可用break跳出迴圈          
        break
    else:
        print(f"我也喜歡吃 {input_msg.title()}")

# ch7_31.py
players = ['Curry','Jordan','James','Durant','Obama','Kevin','Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引index
while index < len(players):             # 是否index在串列長度範圍
    if index == n:                      # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1                          # 索引index加1
    
# ch7_32.py
index = 0
while index <= 10:
    index += 1
    if index % 2:           # 測試是否奇數
        continue            # 不往下執行
    print(index)            # 輸出偶數

'''使用迴圈刪除特定重複內容'''
# ch7_33.py
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print("刪除前的fruits", fruits)
while fruit in fruits:      # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)

#建議
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
[x for x in fruits if x!="apple"]

# ch7_34.py
buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
while buyers:                           # 買家分類完成,迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:          # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)   # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)

''' pass 什麼事都不做，但有時候可以用'''#不介入迴圈控制


# ch7_35.py
schools = ['明志科大', '台灣科大', '台北科大']
for school in schools:
    pass

schools = ['明志科大', '台灣科大', '台北科大']
for school in schools:
    if school == "台灣科大":
        pass #日後新增動作，或是故障排除時暫時的設定
             #(可以當作日後方便利用搜尋來看是否有未完善的地方)
        #print(school)
    else:
        print(school)
        
#7-5 enumerate 物件使用搭配迴圈 
'''自行閱讀'''
# ch7_37.py
scores = [21,29,18,33,12,17,26,28,15,19] 
# 解析enumerate物件
for count, score in enumerate(scores, 1):   # 初始值是 1
    if score >= 20:
        print(f"場次 {count} : 得分 {score}")