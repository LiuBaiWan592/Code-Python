import random

def guess_number():
    number = random.randint(1, 100)
    guess = -1
    while guess != number:
        guess = int(input("请输入你猜的数字："))
        if guess < number:
            print("猜小了！")
        elif guess > number:
            print("猜大了！")
        else:
            print("恭喜你，猜对了！")

guess_number()