class computer:
    def __init__(self, make, model):
        self.make = make          # This will be visible
        self.__model = model    # The two underscores will make this private

    def price(self, amount):
        self.__model += amount

    def get_model(self):
        return self.__model

computer1 = computer("macbook", "pro")
computer2 = computer("dell", "inspiron")

print(computer1.make)
print(computer2.make)
print(computer2.get_model())         
print(computer1.get_model())  

