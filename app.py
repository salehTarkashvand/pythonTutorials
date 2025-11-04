# unpack and enumerate

letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter) # tuple
# (0, 'a')
# (1, 'b')
# (2, 'c')

#iterate with unpack
letters = ["a", "b", "c"]
for index , letter in enumerate(letters):
    print(index) # tuple
# 0
# 1
# 2
