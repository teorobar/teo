# File: homework4.py

# ---Lists---

# --List Operations--
favorite_foods = ["hot dog", "sashimi", "taco", "goldfish", "mango"]
# print(favorite_foods[1])
# print(favorite_foods[-1])
# favorite_foods.append("peach")
# favorite_foods.insert(0, "apple")
# favorite_foods.remove("taco")
# print(len(favorite_foods))
# for food in favorite_foods:
#     print(food.upper())
# foods = [favorite_foods[0],favorite_foods[-1]]
def is_potato(list):
    if "potato" in list:
        print("A Potato!")
    else:
        print("No potato!")
# is_potato(favorite_foods)

# --Slicing and Striding--
nums = list(range(21)) #Fixed error: wrote 20 instead of 21 (needed 0-20 inclusive)
def get_first_15(list):
    first_15 = list[0:15]
    return first_15
def get_every_5th(list):
    every_5th = list[0::5]
    return every_5th
def reverse_and_stride(list):
    reverse = list[::-1]
    every_3rd = reverse[0::3]
    return every_3rd
# print(get_first_15(nums))
# print(get_every_5th(get_first_15(nums)))
# print(reverse_and_stride(get_every_5th(get_first_15(nums))))

# --Nested Lists--
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = [7, 8, 9]

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# -Nested List Operations-
# print(numbers[2]) #Fixed error: indexing mistake
# print(numbers[1][1])
# numbers.append([10, 11, 12])
# print(numbers)
def sum_nested(list):
    sum = 0
    for row in list:
        for num in row:
            sum += num
    return sum
# print(sum_nested(numbers))

# --Create a 5x5 List--
def five_by_five():
    nested = []
    x = 0
    for i in range(5):
        row = []
        for i in range(5):
            x += 1
            row.append(x)
        nested.append(row)
    return nested
grid = five_by_five()

def replace_mults_of_3(nested):
    x = []
    for a in nested:
        row = []
        for b in a:
            num = b
            if num%3 == 0:
                row.append("?")
            else:
                row.append(num)
        x.append(row)
    return x
grid1 = replace_mults_of_3(grid)

def sum_nested(list):
    sum = 0
    for row in list:
        for num in row:
            if num != "?":
                sum += num
    return sum

# ---Dictionaries---

# --Dictionary Operations--
# ages = {
#     "Katie": 30,
#     "Mariam": 42,
#     "Safia": 25,
#     "Mira": 48
# }
# print(ages["Katie"])
# ages["Mira"] = 100
# ages["Milana"] = 52 #Fixed error: tried to use append :)
# del ages["Mariam"]
# for i in ages:
#     print(i)

# print(grid1)