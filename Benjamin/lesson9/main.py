class Calculator:
    def __init__(self, num1, num2):
        
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        self. total = self.num1 + self.num2
        return self.total
    
    def subtraction(self):
        self.total = self.num1 - self.num2
        return self.total
    
    def multiplication(self):
        self.total = self.num1 * self.num2
        return self.total


        
    def get_userinput(self):
        self.num1 = int(
            input("enter first number: ")
        )
        self.num2 = int(
            input("enter first number: ")
        )

        self.message = input(
            "select the operation\n"
            "[+] [-] [*]\n"
        )
    
        if self.message == "+":
            return self.addition



my_calcus = Calculator()

print(my_calcus.get_userinput())
