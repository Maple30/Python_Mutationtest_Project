def get_index(string=None, item=''):
    flag = 0
    all_index = []

    for value in string:
        if string.find(value,flag) != "-1":
           all_index.append(string.find(value,flag))            
           flag =  string.find(value,flag) + 1
    return all_index

a = "AAAffAAAxxc"
print(get_index(a,"A"))