import random 

def game():
    print("Welcome to the Number Guessing Game!")
    score = random.randint(1, 100)

    with open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Hiscore is: {score}")
    if (score>hiscore):
        with open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/hiscore.txt", "w") as f:
            f.write(str(score))
            
    return score

game()

