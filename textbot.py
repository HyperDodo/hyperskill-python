def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("What is the purpose break statement in python?")
    print("1. Terminates the loop statement and transfers execution to the statement immediately following the loop.")
    print("2. Terminates the life on earth.")
    print("3. Terminates the running script immediately.")
    print("4. Breaks the chain of supply between manufacturers and distributors.")
    real_answer = 1
    user_answer = int(input())
    while user_answer != real_answer:
        print("Please, try again")
        user_answer = int(input())
    print('Noice choice mate!')


def end():
    print('Congratulations, have a nice day!')


greet('Celsius', '1984')  # change it as you need
remind_name()
guess_age()
count()
test()
end()