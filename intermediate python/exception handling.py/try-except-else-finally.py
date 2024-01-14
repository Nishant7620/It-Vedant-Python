x = 100
y = 2



try :
    z =x/y
    print(z)
except ZeroDivisionError:
     print("cannot divisible by zero")

else:
    print("else block executed")

finally:
    print("finally block excecuted")    