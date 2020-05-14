#Recommended method using context manager
with open('readable_file.txt','r') as f:
    for line in f:
        print(line,end='')


# #non recommended method using file object

# file = open('readable_file.txt','r')
# print(file.name)

# file.close()
