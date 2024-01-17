print('Hello world')

my_string = "Test string"

print(my_string)

print(my_string[0])

print('This is a test for .format() printing {}'.format('INSERTED'))

my_dict = {'key1':'value1','key2':'value2'}

print(my_dict['key1'])

list_sum = 0

my_iterable = [1,2,3,4,5,6,7,8,9]
for items in my_iterable:
    list_sum = list_sum + items

print(list_sum)


my_list = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in my_list:
    print(b)