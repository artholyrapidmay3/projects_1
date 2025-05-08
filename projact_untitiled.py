class Realestase:
    def __init__(self,address,price,area):
        self.area=area
        self.address=address
        self.price=price
    def show_price(self):
      print(self.price)
    def show_area(self):
       print(self.area)
    def show_address(self):
       print(self.address)
house=Realestase('mashad,ladan St 123',1000000000,'120M')
print(house.address)
print(house.area)
print(house.price)