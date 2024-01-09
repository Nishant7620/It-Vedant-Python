print("{:d}".format(100))
print("{x:d}".format(x=200))
print("{1:d}".format(300,400))
print("{0:6d}".format(200))
print("{0:06d}".format(500))
print("{0:+06d}".format(600))
print("{0:<+06d}".format(600))
print("{0:#<+10d}".format(200))
print("{0:*^+8d}".format(400))
print("{:,}".format(123454354345))
print("{:_}".format(123123423443545))

"""-------------------------------first assigning values then passing values----------------------------------------"""

name="Nishant"
city="Panvel"
print("My name is {}, I live in {}".format(name,city))