def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]


for char in rev_str("hello"):
     print(char)


# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
