def hello():
    print("Hello")

def pack(arg1, arg2, arg3):
    pack_list = [arg1, arg2, arg3]
    return pack_list

empty_list = []
def eat_lunch(empty_list):
    for i in empty_list:
        print("First I eat", i)
        i += 1
        if i <= len(empty_list):
            print("Next I eat", i)
        else:
            print("There's nothing to eat.")
