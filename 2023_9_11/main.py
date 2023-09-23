import time , os
i = 0
minn =60
os.system("cls")
os.system("color a")
print("計時開始!")
while True:
    i += 1
    if i % minn == 0:
        mina = int(i/ minn)
        print(mina,"分鐘")
    else:
        print(i)
    time.sleep(1)
