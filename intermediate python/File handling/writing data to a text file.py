file = open("new text file.txt",mode="w")
file.write("this is new text file")
file.close()

#-------------------------------------------------------------------------
#executing same file in write mode

file = open("new text file.txt",mode="w")
file.write("we have again executed same file with write mode.So it will overide the data")
file.close()

#-------------------------------------------------------------------------
#appending data to a file with mode="a"

file =open("new text file.txt",mode="a")
file.write("Appending data in to....We have created a text file")
file.close()

#----------------------------------------------------------------------------
#Excllusive creation a file with mode="x"

file=open("new text file.txt",mode="x")
file.write("exclusive created file")
file.close()