class House:
    
    city = "Chicago"
    def __init__(self, sqft, price):
        self.__sqft = sqft
        self.__price = price
    @property
    def sqft(self):
        return self.__sqft

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"House in {House.city} with {self.sqft} sqft for ${self.price}"
    
if __name__ == "__main__":
    my_house = House(120, 999)
    print(my_house)
        