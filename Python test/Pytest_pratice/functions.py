def get_index(string=None, item=''):
    flag = 0
    all_index = []

    for value in string:
        if string.find(item,flag) != -1:
           all_index.append(string.find(item,flag))            
           flag =  string.find(item,flag) + 1
        else:break
    return all_index

# def diffculty_option(option = 1):
