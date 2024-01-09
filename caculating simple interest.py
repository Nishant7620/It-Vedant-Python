sets =  3

for i in range(sets):
    p = float(input(f"enter a principal amount for set {i+1}: "))
    n = float(input(f"enter time duration for set {i+1}: "))
    r = float (input(f"enter rate of interest  for set {i+1}: "))

    simple_interest = p*n*r /100
    print(simple_interest)    