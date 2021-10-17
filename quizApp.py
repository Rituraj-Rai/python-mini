from os import getenv
from dotenv import load_dotenv
import sys
import requests as req
from html import unescape as unesc
from random import randrange as rr
from time import sleep

load_dotenv()

wmsg = '''
---------------------------------
Welcome to the Quiz
Enter the correct options to score
Blank will be treated as wrong.
---------------------------------
'''

print(wmsg)
while True:
    try:
        a = int(input('Play?(1/0):'))
        break
    except ValueError:
        print("Oops! Unexpected input.. Try again!")

try:
    res = req.get(getenv('API_URL'))
except:
    sys.exit('Something went wrong!\nCheck your internet connection and try again')


quiz = res.json()['results']

score = 0

if a:
    for q in quiz:
        ci,ua = 0,0
        s = '-'*len(unesc(q['question']))
        print()
        print(s)
        print(unesc(q['question']),'\n')
        opts = [unesc(e) for e in q['incorrect_answers']]
        ci = rr(0,4)
        opts.insert(ci,unesc(q['correct_answer']))
        i = 0
        for opt in opts:
            i+=1
            print(f'{i})',opt)
        try:
            ua = int(input('Enter option number: '))
            print()
        except ValueError:
            print("Oops! Invalid input.. ")
        if ua == ci + 1:
            print("Correct!")
            score += 1
        else:
            print('Wrong answer!')
            print(f'Correct ans: {ci+1}.', opts[ci])
        print(f'Current score: {score}/10')
        sleep(1)
        # sys.exit()
    else:
        print('\n------------------')
        print('Thanks for playing.')
        print(f'Your final score: {score}/10')
else:
    print("Goodbye")