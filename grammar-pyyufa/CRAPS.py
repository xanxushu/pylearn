'''CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进
行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点
数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分
出胜负。'''

#赌博是有赌注的
#初始赌注设置为5000

import random

pay=5000
i=-1

once=int(input("please pay your money!"))
if once<=0 or once>pay:
    print("please text the right number of money!")
    once=int(input())
pay=pay-once
player=[]
player.append(random.randint(1,6)+random.randint(1,6))
i+=1
print("the num is %d"%player[i])
if player[0]==7 or player[0]==11:
    print("player wins!")
elif player[0]==2 or player[0]==3 or player[0]==12:
    print("holder wins!")
else:
    while(pay!=0):
        print("game continues!please pay your money!")
        once=int(input())
        if once<=0 or once>pay:
            print("please text the right number of money!")
            once=int(input())
        pay=pay-once
        player.append(random.randint(1,6)+random.randint(1,6))
        i+=1
        print("you still have %d $ that can be used!\n"%pay)
        print("the num is %d"%player[i])
        if player[i]==player[0]:
            print("player wins!")
            break
        if player[i]==7:
            print("holder wins!")
            break
        if pay==0:
            print("you don't hold money anymore!")
            break