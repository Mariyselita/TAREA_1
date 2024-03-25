def write_list(my_list, fname):
    '''Write a list to a text file'''
    with open(fname, "w", encoding="utf-8") as f:
        for item in my_list:
            f.write(str(item) + '\n')
    print(f"List has been written to {fname}.")

def writeDict(my_dict, fname):
    '''Write a dictionary to a text file'''
    with open(fname, "w", encoding="utf-8") as f:
        for key, value in my_dict.items():
            f.write(f"{key} {' '.join(map(str, value))}\n")
    print(f"Dictionary has been written to {fname}.")

def write_list_of_lists(my_list, fname):
    '''Write a list of lists to a text file'''
    with open(fname, "w", encoding="utf-8") as f:
        for inner_list in my_list:
            f.write(' '.join(map(str, inner_list)) + '\n')
    print(f"List of lists has been written to {fname}.")

if __name__ == '__main__':
    pass
