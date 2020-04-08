from sys import exit

def start():
    print("你是北凉城的一位世子，名为徐凤年，请选择你的人生志向")
    print("a:大爷腰穿万贯，当然要享受荣华富贵 b:虽然家境显赫，但我钟爱文学 ")
    print("c:志向远大的我要游历四方，钻研武学，做一名陆地神仙 d:碌碌无为，过着枯燥的生活")
    choice = input(">")

    if choice == "a":
        rich()
    elif choice == 'b':
        Study()
    elif choice == 'c':
        Go()
    else :
        Do_nothing()



def dead(why):
    print(why)
    exit(0)

def Chun_hua_lou():
    print("选择一位骄人：")
    print("a:春月 b：冬雪")

    choice = input(">")

    if choice == "a":
        dead("春月是一名刺客，为了给亡国复仇，对你进行了刺杀")
    else:
        print("你与冬雪一见钟情，并纳做小妾")
        exit(0)

def rich():
    print("依然是纸醉金迷的一天，今天你要去做什么？")
    print("a:到忘归楼喝到天荒地老  b:去春花楼宠幸骄人")
    choice = input(">")

    if choice == "a":
        dead("喝到了假酒，中毒身亡")

    else:
        Chun_hua_lou()

def Study():
    print("选择一个技能：a:围棋 b：作诗")
    choice = input(">")

    if choice == "a":
        print("天赋异禀，棋艺精湛，从未败北，达到棋圣境界")
        exit(0)

    else:
        print("五步即可作诗一首，召入皇宫，得到大臣们的赏识")
        exit(0)

def Go():
    print("有位凶神恶煞的老人同行，是否同意 y/n")

    choice = input(">")

    if choice == "y":
        print("该人是剑神李淳罡，传授你武林绝学，登上了剑道巅峰，飞升成陆地神仙")
        exit(0)
    else:
        dead("只身前往，惨遭不测")

def Do_nothing():
   dead("父亲惨遭朝廷打压，失去全为，同时你也失去了荣华富贵的生活，最终在贫穷中死去")

start()










