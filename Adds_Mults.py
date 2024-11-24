# The end goal of this is to create a function that takes an array and finds the minimal amount of times 
# you need to add 1 and multilpy by 2 to get that number.
# For example to get to 5 you need to add 1, then multiply by 2 to get 2, multiply by 2 to get 4 then add 1
# to get 5 adding up to a grand total of 4

def add_mult(values):
    vals = list()
    for i in values:
        num = 0
        checker = 0
        while checker != 1:
            if i == 0:
                vals.append(num)
                checker = 1
            elif i % 2 == 0:
                i = i /2
                num += 1
            else:
                i -= 1
                num += 1
    return vals

tests = [15, 20, 11, 11, 5, 14, 17, 6, 8, 4, 7, 17, 18, 16, 3, 2, 11, 12, 14, 12] 

print(add_mult(tests))

