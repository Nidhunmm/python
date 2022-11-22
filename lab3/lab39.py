test_list = ['gf\ng', 'i\ns', 'b\nest', 'fo\nr', 'geeks\n']
 
# printing original list
print("The original list : " + str(test_list))
 
# Removing newline character from string
# using loop
res = []
for sub in test_list:
    res.append(sub.replace("\n", ""))
 
# printing result
print("List after newline character removal : " + str(res))