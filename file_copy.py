# File Copy Program in Python

# open source file in read mode
f1 = open("a.txt", "r")

# open destination file in write mode
f2 = open("b.txt", "w")

# read content from a.txt
data = f1.read()

# write content to b.txt
f2.write(data)

# close both files
f1.close()
f2.close()

print("File copied successfully!")
