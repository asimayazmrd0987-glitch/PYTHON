word = "Cat"

with open("/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O/Cat.txt", "r") as j: 
    content = j.read()
    content2 = content.replace(word, "Dog")

with open("/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O/Cat.txt", "w") as j:
    j.write(content2)
    print(content2)