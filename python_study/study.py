class Unit:
    def __init__(self,name,hp): #__init__ : 생성자
        self.name=name
        self.hp=hp


class AttackUnit(Unit):
    def __init__(self,name,hp,damage): #__init__ : 생성자
        Unit.__init__(self,name,hp)
        self.damage=damage
    
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다".format \
            (self.name,location,self.damage))

    def damaged(self, damage):
        print("{}: {} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{} : 현재체력은 {} 입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed
    
    def fly(self,name, location):
        print("{}: {} 방향으로 날아갑니다.속도 : {}"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)



firebat1=AttackUnit("firebat",50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)