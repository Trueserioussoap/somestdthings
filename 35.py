def get_multiplied_digits (number):
    str_number=str(number)
    str_number=str_number.replace('0','')
    #print(str_number)
    if len(str_number)>1:
        first=int(str_number[0])
        return first*get_multiplied_digits(int(str_number[1:]))
    else:
        return (int(str_number))

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(420)
print(result)
