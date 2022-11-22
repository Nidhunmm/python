color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('lab35.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('lab35.txt')
print(content.read())
