#creating a binary file in mode="w"

file =open("new binary file.txt",mode="wb")
file.write(b"This \nis \tbinary \\file ")
file.close()

#-----------------------------------------------------------------------------
#executing same file in same mode="w"
file =open("new binary file.txt",mode="wb")
file.write(b"This \nis \tbinary \\file ")
file.close()

#-----------------------------------------------------------------------------
#Appending data to a file with mode="a"
file=open("new binary file.txt",mode="ab")
file.write(b"appended \ndata")
file.close()

#----------------------------------------------------------------------------
#Exclusive creation of a file with mode="x"

file=open("new binary file.txt",mode="xb")
file.write(b"exclusively created file")
file.close()