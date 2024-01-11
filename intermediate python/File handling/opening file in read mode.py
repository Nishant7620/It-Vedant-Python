file = open("text file.txt",mode = "w")

file.write("hello \nworld")
file.close()


file = open("text file.txt",mode="r")
print(file.read())