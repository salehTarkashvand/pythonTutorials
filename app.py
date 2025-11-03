# keyword argument unpacking (**args)


def save_user(**user): 
    print(user)  # {'id': 1, 'name': 'saleh', 'age': 26}
    print(user["name"])  # saleh



save_user(id=1, name="saleh", age=26)  # 240
