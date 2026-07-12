marks = {}

marks1=int(input("Enter marks for Math :"))
marks2=int(input("Enter marks for Physics :"))
marks3=int(input("Enter marks for Computer Science :"))

marks.update({"Math":marks1})
marks.update({"Physics":marks2})
marks.update({"Computer Science":marks3})

print(marks)