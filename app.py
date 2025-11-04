# add and remove from list


                #add

#append
letters = ["a", "b", "c"]

letters.append("b")
print(letters)  # ['a', 'b', 'c', 'b']

#insert
letters = ["a", "b", "c"]

letters.insert(0,"b")
print(letters)  # ['b', 'a', 'b', 'c']

            #remove

#pop
letters = ["a", "b", "c"]

letters.pop()
print(letters)  # ['a', 'b']

#pop(index)
letters = ["a", "b", "c"]

letters.pop(0)
print(letters)  # ['b', 'c']

#remove
letters = ["a", "b", "c"]

letters.remove("c")
print(letters)  # ['a', 'b']

#del letters[index or :2 ]
letters = ["a", "b", "c"]
del letters[2] #['a', 'b']
del letters[:2] #['c']
print(letters)

