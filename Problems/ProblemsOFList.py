
#length of list in python
list=[1,2,3,4,3,2,2,23,2,2]
counter =0
for item in list:
    counter=counter+1
print(counter)

#check if element exist in list in python
list=[21,32,32,23,35,3,2,21,22,1]
element=2
for item in list:
    if item == element:
        print("Found it!!")
        break

#reversing a list in python with some code

list=[2,32,21,23,23]

list2=[0,0,0,0,0]
print(list2,"list 1",list)
counter=4
for item in list:
    list2[counter]=item
    print(list2,list, counter)
    counter=counter-1

print(list2)
