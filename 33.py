def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#1
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
#2
values_list =(1, 'строка', True)
values_dict ={'a':11,'b':23,'c':42}
print_params(*values_list)
print_params(**values_dict)
#3
values_list_2 =(1,True)
print_params(*values_list_2, 42)
