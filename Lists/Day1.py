#adding an element into a list:

# list = []
# list.append(20)
# print(list)
# list.append("abc")
# print(list)

# a = list((10))
# print(a)``


abc = []

# abc.append(12)
# abc.insert(0, 11)
# print(abc)
abc.extend([10, "Satyam", 30])


abc.reverse()
# print(abc)

abc.pop(0)
print(abc)

# abc.remove()



a = [12, 22 ,32, 42, 55, 62, 72]
a[4] = 52
print(a)


list = ["banana", "Apple", "Sunil"]

for i in list:
    print(i)

list = []
n = int(input("Enter the length of list: "))
for i in range(n):
    elem = input("Enter the element: ")
    list.append(elem)
print(list)

initial = 1
destination = int(input("Enter the last number (n) : "))
user_list = []

for i in range(initial, destination+1):
    user_list.append(i)
print(user_list)

list = [12,3,5,10,2,3,6,7,5,9]
list.sort(reverse=True)
print(list)