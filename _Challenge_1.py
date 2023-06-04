def add_25_fun(num):
    add_25 = lambda x: x + 25
    return add_25(num)
input_num = 10
result = add_25_fun(input_num)
print(result)