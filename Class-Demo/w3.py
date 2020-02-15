# 1. Make a Class that processes Employee Details (3 employees will do)
# 2. Make a function that creates instances of that class from a Dictionary
# 3. Use the function to display the new Details
# 4* Make a new dictionary with the new values? 

employees = {"Dr Pi":49000, "Bob Marshall" : 22000, "Tommy Vance" :33000}

class Worker(object):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1 + percent)

    def firstname(self):
        return self.name.split()[0]
    
def display():
    employeesV2 = {}
    for keys, values in employees.items() :
        en = keys.split()[0]
        print("Instance Name = ", en)
        en = Worker(keys, values)
        en.give_raise(0.12)
        print("Employee Name = ", en.name)
        print("Original Salary =", values)
        print("Employee New Salary = ", int(en.pay))
        print("-" * 30)
        #employeesV2.update({keys, values})
    print(employeesV2)

    
    

display()
