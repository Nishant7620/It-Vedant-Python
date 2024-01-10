file = []

for i in range(2):
    file.append(input("enter a name: "))

print(file)  

#------------------------------------------------------------------------
#creating a file

file = open("Demo file.txt",mode="w")
file.write("we have created text file")
file.close()