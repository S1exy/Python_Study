

import random
import time

i = 0  # 在全局作用域中定义i




class Pokemon:
    def __init__(self, name, hp, attack, defense, element, dodge_rate):
        self.name = name             #名字
        self.max_hp = hp            #最大血量
        self.hp = hp                #血量
        self.attack = attack        #攻击力
        self.defense = defense      #防御
        self.element = element      #属性
        self.dodge_rate = dodge_rate#躲闪率
        self.status_effects = []    #当前状态
        self.move = []              #技能
        self.protime = 1

    # 草元素回血
    def add_hp(self):
        if self.element == "草":
            self.hp = self.hp * 1.1
            self.hp = round(self.hp, 2)
            print(f"{self.name}触发了草元素被动回复了{ self.hp*0.1 }点血,现在的血量为{self.hp}")




    # 火元素增伤
    def add_attack(self):
        i = 0
        if i == 4:
            print("{self.name}的增伤已经达到极限40%了")
        else:
            if self.element == "火":
                self.attack = self.attack * 1.1
                self.attack = round(self.attack,2)
                print(f"{self.name}触发了火元素被动 伤害增加了{self.attack / 1.1 * 0.1} 现在伤害为{self.attack}")
                i = i + 1


    def judge(self,other):
        """闪避值判断："""
        b = random.randint(1 , 100)
        if b <= other.dodge_rate:
            return False
        if b > other.dodge_rate:
            return True

    # 元素判断进行伤害加减
    def yuansu(self,other):
        """元素对于攻击力的判断"""
        if self.element == "电":
            #增加攻击力
            if other.element == "水":
                self.protime = 2
                print(f"你的 {self.element} 克制对方的 {other.element} 元素 你的伤害翻倍了！")
            if other.element == "草":
                self.protime = 0.5
                print(f"你的 {self.element} 被对方的 {other.element} 元素克制 你的伤害减少了50%")

        if self.element == "草":
            #增加攻击力
            if other.element == "水":
                self.protime = 2
                print(f"你的 {self.element} 克制对方的 {other.element} 元素 你的伤害翻倍了！")
            if other.element == "火":
                self.protime = 0.5
                print(f"你的 {self.element} 被对方的 {other.element} 元素克制 你的伤害减少了50%")

        if self.element == "火":
            #增加攻击力
            if other.element == "草":
                self.protime = 2
                print(f"你的 {self.element} 克制对方的 {other.element} 元素 你的伤害翻倍了！")
            if other.element == "水":
                self.protime = 0.5
                print(f"你的 {self.element} 被对方的 {other.element} 元素克制 你的伤害减少了50%")

        if self.element == "水":
            #增加攻击力
            if other.element == "火":
                self.protime = 2
                print(f"你的 {self.element} 克制对方的 {other.element} 元素 你的伤害翻倍了！")
            if other.element == "电":
                self.protime = 0.5
                print(f"你的 {self.element} 被对方的 {other.element} 元素克制 你的伤害减少了50%")

    # 元素攻击进行回调
    def reyuansu(self,other):
        self.protime = 1
        other.protime = 1

    # 伤害大模块
    def attack_move(self, other, n):
        global i
        # 闪避判断
        if self.judge(self):
            # 元素克制判断
            self.yuansu(other)
            damage = self.attack * self.move[n]["time"] * self.protime - other.defense
            if damage < 0:
                damage = 0
                print("此次攻击造成了 0 点伤害 未能击穿敌军护甲！")
            else:
                # 水元素减伤
                if other.element == "水":
                    damage = damage * 0.7
                    print(f"{other.name}触发了水元素被动 受到的伤害减少了{damage / 0.7 * 0.3} 现在受到的伤害为{damage}")
                other.hp = other.hp - damage
                print(f"{self.name} 对 {other.name} 造成了 {damage} 点伤害，太痛了")

                print(f"{other.name} 剩余血量：{other.hp}")
                # 火元素增伤
                self.add_attack()
        else:
            print(f"{self.name} 对 {other.name} 的攻击被闪避了哦")
            print(f"{other.name} 剩余血量：{other.hp}")

            # 电元素闪电五连板
            if other.element == "电":
                print(f"{other.name}闪避成功 触发了电元素被动 可以对敌人再次发动一次技能")
                if (i % 2) == 1:
                    print(f"你的 {other.name} 拥有如下技能:")
                    print(f"1. {other.move[0]["name"]} \n2. {other.move[1]["name"]}")
                    print("选择一个技能进行攻击:")
                    tem = int(input())
                    # 玩家攻击
                    print(f"{other.name} 使用了 {other.move[tem - 1]["name"]} !")
                    other.attack_move(self, tem - 1)
                    i = i -1
                if (i % 2) == 0:
                    print(f"{other.name} 使用了 {other.move[random.randint(0, 1)]["name"]} !")
                    other.attack_move(self, random.randint(0, 1))
        i = i + 1
        # 元素攻击倍率回调
        self.reyuansu(other)

    # 结束模块：
    def ending(self,other):
        if self.hp <= 0:
            print(f"你的宝可梦 {self.name} 被打败了 陷入了昏厥 ")
            return 1
        if other.hp <= 0:
            print(f"电脑的宝可梦 {other.name} 被打败了 陷入了昏厥 ")
            return 2


class ElectricPokemon(Pokemon):               # 皮卡丘（电）
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, ' 电 ', 30)
        self.name = "皮卡丘"  # 名字
        self.max_hp = 80  # 最大血量
        self.hp = 80  # 血量
        self.attack = 35  # 攻击力
        self.defense = 5  # 防御
        self.element = "电"  # 属性
        self.dodge_rate = 30  # 躲闪率
        self.status_effects = []    #当前状态
        self.move = [{"name":"十万伏特","time": 1.4,"pro":"麻痹效果"},{"name":"电光一闪","time": 1.0,"pro":"快速攻击"}]
        self.protime = 1

class GrassPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, ' 草 ', 10)
        self.name = "妙蛙种子"  # 名字
        self.max_hp = 100  # 最大血量
        self.hp = 100  # 血量
        self.attack = 35  # 攻击力
        self.defense = 10  # 防御
        self.element = "草"  # 属性
        self.dodge_rate = 10  # 躲闪率
        self.status_effects = []  # 当前状态
        self.move = [{"name": "种子炸弹", "time": 1.0, "pro": "中毒"},
                     {"name": "寄生种子", "time": 0.0, "pro": "寄生"}]
        self.protime = 1

class WaterPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, ' 水' , 20)
        self.name = "杰尼龟"  # 名字
        self.max_hp = 80  # 最大血量
        self.hp = 80  # 血量
        self.attack = 25  # 攻击力
        self.defense = 20  # 防御
        self.element = "水"  # 属性
        self.dodge_rate = 20  # 躲闪率
        self.status_effects = []  # 当前状态
        self.move = [{"name": "水枪", "time": 1.4, "pro": "无"},
                     {"name": "护盾", "time": 0, "pro": "护盾"}]
        self.protime = 1


class FirePokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense, ' 火 ', 10)
        self.name = "小火龙"  # 名字
        self.max_hp = 80  # 最大血量
        self.hp = 80  # 血量
        self.attack = 35  # 攻击力
        self.defense = 10  # 防御
        self.element = "火"  # 属性
        self.dodge_rate = 10  # 躲闪率
        self.status_effects = []  # 当前状态
        self.move = [{"name": "火花", "time": 1.0, "pro": "烧伤"},
                     {"name": "蓄能爆炎", "time": 0, "pro": "烧伤pro"}]
        self.protime = 1

# 定义概率函数：
def p(n):
    """闪避值判断："""
    b = random.randint(1, 100)
    if b <= n:
        return True
    if b > n:
        return False

# 选择宝可梦第一个模块
def choose():    #挑选英雄函数
    bag = []
    c = ["皮卡丘","妙蛙种子","杰尼龟","小火龙"]
    print("请选择3个宝可梦用于组成你的队伍：")
    print("1.皮卡丘(电属性) 2.妙蛙种子(草属性) 3.杰尼龟(水属性) 4.小火龙(火属性)")
    print("请选择你的宝可梦（选择3只）： 中间以空格作为间隔")
    a = input().split()
    tem = []
    print("你选择的宝可梦分别是：")
    if (a[0] == "1") or (a[1] == "1") or (a[2] == "1"):
        print("1.皮卡丘(电属性)")
        tem.append(0)
    if (a[0] == "2") or (a[1] == "2") or (a[2] == "2"):
        print("2.妙蛙种子(草属性)")
        tem.append(1)
    if (a[0] == "3") or (a[1] == "3") or (a[2] == "3"):
        print("3.杰尼龟(水属性)")
        tem.append(2)
    if (a[0] == "4") or (a[1] == "4") or (a[2] == "4"):
        print("4.小火龙(火属性)")
        tem.append(3)


    print("请选择你的宝可梦：")
    print(f"1.{c[tem[0]]} 2.{c[tem[1]]} 3.{c[tem[2]]}")
    print("输入数字选择你的宝可梦：",end="")
    b = int(input())
    print(f"你选择了 {c[tem[b - 1]]}")

    numbers = [i for i in range( 0 , 3 ) if i not in [tem[b - 1]]]
    random_number = random.choice(numbers)

    print(f"电脑选择了：{c[random_number]}")
    return [tem[b - 1],random_number]


#游戏开始啦
def start():
    a = [
        ElectricPokemon(name="皮卡丘", hp=80, attack=35, defense=15),
        GrassPokemon(name="妙蛙种子", hp=80, attack=25, defense=20),
        WaterPokemon(name="杰尼龟", hp=100, attack=35, defense=10),
        FirePokemon(name="小火龙", hp=80, attack=35, defense=5)]
    choose_end = (choose())
    b = a[choose_end[0]]
    c = a[choose_end[1]]

    # 回合开始：
    for i in range(1 , 100):
        print(f"这是第 {i} 个回合")

        #回血模组
        a[choose_end[0]].add_hp()

        #战斗模组
        fight(choose_end,a)

        # 空隙模块
        print("")
        print("")

        # 判断结束（回合完全结束）
        tem = a[choose_end[0]].ending(a[choose_end[1]])
        if tem == 1:
            break
        if tem == 2:
            break





def time_sleep():
    """# 等待阶段 使函数暂停2s"""
    time.sleep(2)


#战斗模块
def fight(choose_end,a):
    print(f"你的 {a[choose_end[0]].name} 拥有如下技能:")
    print(f"1. {a[choose_end[0]].move[0]["name"]} \n2. {a[choose_end[0]].move[1]["name"]}")
    print("选择一个技能进行攻击:")
    tem = int(input())
    # 玩家攻击
    print(f"{a[choose_end[0]].name} 使用了 {a[choose_end[0]].move[tem - 1]["name"]} !")
    a[choose_end[0]].attack_move(a[choose_end[1]], tem - 1)
    # 等待
    time_sleep()
    print("")
    # 电脑攻击
    print(f"{a[choose_end[1]].name} 使用了 {a[choose_end[1]].move[random.randint(0,1)]["name"]} !")
    a[choose_end[1]].attack_move(a[choose_end[0]], random.randint(0,1))


# 主函数 全部实现的阶段：
def main():
    start()


main()


