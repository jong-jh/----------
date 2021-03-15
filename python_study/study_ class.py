class House:
    def __init__(self,location,house_type,deal_type,\
        price,complecation_year):
        self.location = location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.complecation_year=complecation_year

    def show_detail(self):
        print("{} {}".format(self.price,self.complecation_year))

house=[]
house1=House("강남","아파트","매매","10억","2010년")
house2=House("마포","오피스텔","전세","5억","2007년")

house.append(house1)
house.append(house2)

for i in house:
    i.show_detail()