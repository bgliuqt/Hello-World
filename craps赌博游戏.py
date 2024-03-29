'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。

简单的规则是：
1、玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
2、玩家第一次如果摇出2点、3点或12点，庄家胜；
3、其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
4、如果玩家摇出了第一次摇的点数，玩家胜；
5、其他点数，玩家继续要骰子，直到分出胜负。

'''

from random import randint

# 设定赌资1000
money = 1000

while money > 0:
    
    print('您当前的总资产为：', money)
    
    needs_go_on = False
    
    while True:
        
        debt = int(input('请下注：'))
        
        if 0 < debt <= money:
            break
        else:
            print('请正确下注，不要捣乱!')
            
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    
    if first == 7 or first ==11:
        print('玩家胜！！')
        money += debt
    elif first ==2 or first ==3 or first == 12:
        print('庄家胜！')
        money -= debt
    else:
        needs_go_on = True
        print('未分胜负，继续摇~')
    
    while needs_go_on:
        
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        
        if current ==7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
            print('未分胜负，继续摇~')
            
print('输完了吧~，游戏结束，请勿赌博')
        
    
