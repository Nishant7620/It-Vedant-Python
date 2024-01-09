details = {"Sahil":7620750234,"Manish":9920906471,"Mitesh":7620750145,"Rahul":9920906352}

mykeys = list(details.keys())
mykeys.sort()
sorted_dict = {i: details[i] for i in  mykeys}

user_input =input("enter your name: ")

if user_input in sorted_dict:
    print(sorted_dict[user_input])

else:
    if user_input not in sorted_dict:
        print("your details are not present in dictionary we have mention your name please enter your phone number")
        value = int(input("enter a phone number: "))
        sorted_dict.setdefault(user_input,value)
    print(sorted_dict)    
