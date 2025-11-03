# while operator

number = 100
while number > 0:
    print(number)
    number //= 2

print("Done")

# 100
# 50
# 25
# 12
# 6
# 3
# 1
# Done



command = ""

while command.lower() != "exit":
    command = input(">>>")
    print(command)
    if command.lower() == "Exit":
        break

print("Done")
