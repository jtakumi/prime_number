import time
import random,json,datetime,math

today = datetime.datetime.today()
d= today.strftime("%Y_%m_%d")
print("Today is " + d)
while(True):
    q=random.randint(13,200000)
    c=0
    #素数判定はその数の平方根までを調べればよし
    sq = int(math.sqrt(q))
    for i in range(2,sq,1):
        if sq % i == 0:
            print(q, " is prime number.")
            c=1
            break
        else:
            if i > 2:
                i += 1
    if c==0:
        print(q,"is normal number.")
    time.sleep(1)