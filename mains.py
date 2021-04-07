import random
import time
import datetime

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

def localtime():
    time = datetime.datetime.now()
    return f'[{time.strftime("%H:%M:%S")}]'

def generator(number: int):
    num = 0
    for a in range(number):
        num += 1
        TOKEN = ''

        for a in range(30):
            TOKEN+=random.choice(chars)
        TOKEN+=''

        time.sleep(0.0)
        print(f'{TOKEN}')

def main():
    number = int(input('>>> '))
    print('='*75)
    generator(number)
    print('='*75)
    main()

if __name__ == '__main__':
    print('Twitch-token-generator')
    print('How many tokens do you need?')
    main()
