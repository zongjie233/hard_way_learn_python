ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","banana","Girl","boy"]

while len(stuff) != 10:
    #pop()默认最后一个元素
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")


print("There we go:",stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print(' '.join(stuff))
print(' 123'.join(stuff))
print('#'.join(stuff[3:5]))







