# code 14-1-1
"""
class Waffle:
    name = "waffle"

choco = Waffle()
print(choco.name)

banana = Waffle()
print(banana.name)
"""

"""
# code 14-2-1
class Waffle:
    def setName(self, n):
        self.name = n

choco = Waffle()
choco.setName("choco waffle")
print(choco.name)

banana = Waffle()
banana.setName("banana waffle")
print(banana.name)

# code 14-2-2
class Avatar:
    def setAvatar(self, height, skill):
        self.height = height
        self.skill = skill
    
    def printAvatar(self):
        print("키는", self.height, "cm, ", "스킬은", self.skill, "입니다.")

byunsoo = Avatar()
byunsoo.setAvatar(120, '점프')
byunsoo.printAvatar()
"""

# code 14-3-1, 14-3-3
class Avatar:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def increaseHp(self):
        self.hp = self.hp + 10
    
    def decreaseHp(self):
        self.hp = self.hp - 10
    
    def printHp(self):
        print("현재", self.name, "의 hp는", self.hp, "입니다.")

byunsoo = Avatar("byunsoo", 0)
byunsoo.printHp()

pythony = Avatar("pythony", 0)
pythony.printHp()