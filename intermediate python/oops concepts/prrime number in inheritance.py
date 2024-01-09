class Number:
    def user_input(self,num):
        self.num = num
        
class Prime(Number):
    def Is_prime(self):
        if self.num<=1:
            return True
        else:
            for i in range(2,self.num):
                if self.num%i==0:
                    return False
            return True

    if Is_prime(num):
        print("true")
    else:
        print("false")

x =Number(5)