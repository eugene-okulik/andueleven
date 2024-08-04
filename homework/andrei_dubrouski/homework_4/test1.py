my_dict = {'tuple': (1, 5, 3, True, 11, None, 'text1', 2.67), 'list': [False, 34, 4.55, 'text2', 7, 91, None],
           'dict': {'one': 1, 'two': 2, 'three': 44, 'four': True, 'five': 89},
           'set': {59, 4, 10, True, 9.81, 23, None}}

print(my_dict['tuple'][-1])

my_dict['list'].append('new_element')

my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'new_value'

my_dict['set'].add(45678)

my_dict['set'].remove(9.81)

print(my_dict)
