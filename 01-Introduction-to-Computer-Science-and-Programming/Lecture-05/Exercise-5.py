# Printing every even index of a string

my_str = "abcdefg"

new_str = ""
for i in range(0, len(my_str), 2):
    new_str += my_str[i]

print(new_str)