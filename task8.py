
class Moneyfmt:
    def __init__(self,data_value):
        self.data_value = data_value
    
    def update(self,new_value):
        self.data_value  = new_value

    def repr(self):
        print(self.data_value)

     #that  implements logic of the dollarize method - реализует

    def dollarize (self):
        convert = '${:,.2f}'.format(self.data_value)
        print(convert)

obj = Moneyfmt(12345678.021)
print(obj.data_value)
obj.update(100000.4567)
print(obj.data_value)
obj.dollarize()










# money = float(1234.5)
# print(money) #output is 1234.5
# '${:,.2f}'.format(money)
# print(money) #output is 1234.5
