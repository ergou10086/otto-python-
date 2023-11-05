import random
def otto跟你做游戏():
    i = 0
    key = random.randint(1,10)
    while i < 5:
        guss = int(input("enter:"))
        if key == guss:
            print("我草，冰！！！")
            break
        elif guss > key:
            print("guss > key  铸币吧队友呢救一下啊")
        else:
            print("guss < key 他都这样了你为啥不顺从他呢")
        i += 1
    else:
        print("阿弥诺斯，你击败就是白字")
        print('The key is: ' , key)
otto跟你做游戏()
