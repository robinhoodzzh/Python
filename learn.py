# 请独立完成这个产品吧，我相信你可以的！
import random
def recommend():
    print('那么，接下来我作为AI来向你推荐一下今天可以吃的！')
    menu={
    1:'叫花鸡',
    2:'宫保鸡丁',
    3:'照烧鸡',
    4:'火锅鸡',
    5:'黄焖鸡'
    }
    for i in menu:
        print(str(i)+':'+menu[i])
    choose=input('让我随机推荐，还是您先选择一个范围？随机=1，范围=2\n')
    if choose=='1':
        print('为您推荐的是'+menu[random.randint(1,len(menu))])
        print('推荐结束！爱吃不吃！88！')
    else:
        ii=[]
        print('选择以上菜单的编号，我来为你选择一个！\n')
        while True:
            chooserange=input('一个个编号来，输入一个编号按一次回车，完了输入0\n')
            num=int(chooserange)
            if num in range(1,len(menu)):
                ii.append(num)
            elif chooserange=='0':
                if ii:
                    break
                else:
                    print('什么都没选啊！重新输入\n')
            else:
                print('菜单上木有这个！你是不是想自己做？重新输入\n')
        final=random.choice(ii)
        print('给您选好了的菜是:%s，那么下次再见！'%(menu[final]))
        

    
def main(choice):
    #choice= input('今天你知道要吃啥不？(Y or N)')
    if choice == 'Y' or choice == 'y':
        print('好的，祝您用餐愉快！再见\n')
        return(1)
    elif choice == 'N' or choice == 'n':
        recommend()
        return(2)
    else:
        print('您的回答无法理解，请重新选择。知道吃啥不？(Y or N)\n')
        return(3)


while True:
    choice= input('今天你知道要吃啥不？(Y or N)\n')
    choose=main(choice)
    if choose == 3:
        pass
    else:
        break
                 
    
    

    
