# read a text-file
file = open('data.txt', 'r')
print(file.read())
file.close()
print(file.closed)   # is file closed?
