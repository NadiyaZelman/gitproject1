# Return Values


def full_name(first, last):
    """Returns full name"""
    # print(f"{first.title()} {last.title()}")
    return f"{first.title()} {last.title()}"


def adding(a, b):
    return a + b


# def full_name_dict(first, last):
def full_name_dict(first: str, last: str) -> dict:
    """Returns dictionary with first_name, last_name name"""
    result = {'first_name': first.title(), 'last_name': last.title()}
    return result


# 2 + 3 = 5
# (a + b)^2 = a*a + 2*a*b + b*b


# public hashmap full_name_dict(String first, String last){
#     //java code here, example of java code, 1 of the reasons java is called Typed Language
# }

# full_name('anvar', 'nosirov')
# name = full_name('john', 'doe')
# # removed_value=list.pop()
# print(f"{name}, Welcome to the class!")

# total = adding(456, 987)
# print(f"Total is {adding(546, 987)}")
# student1 = full_name_dict('tatiana', 'shark')
# student1 = full_name_dict(456, 777)
# print(student1)
# print(student1['first_name'])
# full_name_dict()


def find_num(num_list, number):
    for num in num_list:
        if num == number:
            print(f"{number} is found!!")
            break


# nums = [5, 55, 76, 1, -9, 0, 1, 456]
# find_num(nums, 1)
# find_num([45, 0, 'hello'], 7)


# passing arbitrary number of arguments
def desc_pizza(*toppings):
    print("We have only cheese pizza with following toppings: ")
    print(*toppings)

# desc_pizza('chicken')
# desc_pizza('chicken', 'peperoni', 'bbq chicken')
# print('hello', 45, ['john', 'doe'], 'world')
