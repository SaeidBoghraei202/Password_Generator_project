import random
import string
from unittest import case

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "@#!$%^&*()++=-^!"
numbers = "0123456789"

all = lower + upper + symbols + numbers


def menu():
    print('ساخت پسورد نیرومند : [1]')
    print('خروج از برنامه : [2]')
    print('_' * 40)
    try:
        choice = int(input('درخواست خود را وارد نمایید : '))
        print('_' * 40)
        if choice < 1 or choice > 2:
            print('مقدار وارد شده خارج از بازه 1 تا 2 میباشد!')
            return None
        return choice
    except ValueError:
        print('مقدار وارد شده نامعتبر میباشد !')
    except Exception:
        print('خطا')


while True:
    choice = menu()

    match choice:

        case 1:
            lenth_Password = int(input('طول پسورد مد نظر خود را وارد نمایید : '))
            password = "".join((random.sample(all, lenth_Password)))
            print(password)
        case 2:
            print('برنامه بسته شد ')
            break
