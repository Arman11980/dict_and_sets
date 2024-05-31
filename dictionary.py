my_set = {1,2,(3,4),'string',1,2,3,4,5,6,7, False}
print(my_set)
print(my_set.update((8, 9)))
print(my_set)
print(my_set.discard(1))
print(my_set)

my_dict = {'cocound': 'кокос', 'apple': 'яблоко', 'pear': 'груша', 'mango': 'манго'}
print(my_dict)
print(my_dict['cocound'])
my_dict.update({'peach' : 'персик', 'cherry' :'вишня'})
print(my_dict)
del my_dict['apple']
print(my_dict)