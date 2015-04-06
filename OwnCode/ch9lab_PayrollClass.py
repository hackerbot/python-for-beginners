#name
#hourly wage
#hours/week
#overtime? >40
#1.5xwage for overtime

#print name
#print hours worked at what wage
#print total wage earned

#repeat, but for overtime

#total earned

class Payroll:
    def __init__(self,name,wage,time):
        self.name = name
        self.wage = wage
        self.time = time
        if self.time > 40:
            self.overtime = self.time - 40 #overtime
        else:
            self.overtime = 0
    def pay(self): #regular pay
        if 40 >= self.time:
            self.pay = self.wage * self.time
        else:
            self.pay = self.wage * 40
        return self.name, 'earned', self.pay, 'during his regular work.'
    def overpay(self): #overtime pay
        if 40 >= self.time:
            return self.name, 'did not work overtime.'
        else:
            self.overpay = self.wage * self.overtime * 1.5 #50% wage increase
            return self.name, 'earned', self.overpay, 'in overtime.'
    def totalpay(self):
        if  self.time > 40:
            self.totalpay = self.pay + self.overpay
            return 'All together', self.name, 'earned', self.totalpay, 'with overtime.'
        else:
            self.totalpay = self.pay
            return 'All together', self.name, 'earned', self.totalpay, 'with no overtime.'
        
person1 = Payroll('Ninh',50,40) #name,wage,time
print(person1.pay())
print(person1.overpay())
print(person1.totalpay())

person2 = Payroll('Hannah',20,60) #name,wage,time
print(person2.pay())
print(person2.overpay())
print(person2.totalpay())