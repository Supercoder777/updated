file =  open('testfile.txt')
#read content of of file

#print(file.read())

print(file.readline())
print(file.readline())

#print line by line

# to print multiple lines

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

#values = [boy, is, so, big, he, fight, with, a, police]
for line in file.readlines():
    print(line)











file.close()