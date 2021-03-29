username = input('User Name : ')
password = input('Password : ')
if username == 'goku' and password == '1234' :
    print('--------------------------------------')
    print('Hello Mr.Goku, Welcome to Z shop')
    print('Shopping menu')
    print('1.Apple     12 THB')
    print('2.Banana    20 THB')
    print('3.Orange    15 THB')
    print('4.Papaya    25 THB')
    print('5.Exit')
    buy = input('Please input the number of fruit you want to buy :')
    if buy == '1':
        quantity = int(input('How many apple you want : '))
        apple_price = 12*quantity
        print('total price is :', apple_price,'THB')
    elif buy == '2':
        quantity = int(input('How many banana you want : '))
        banana_price = 20*quantity
        print('total price is :', banana_price,'THB')
    elif buy == '3':
        quantity = int(input('How many orange you want : '))
        orange_price = 15*quantity
        print('total price is :', orange_price,'THB')
    elif buy == '4':
        quantity = int(input('How many papaya you want : '))
        papaya_price = 20*quantity
        print('total price is :', papaya_price,'THB')
    else:
        print('Thank you for welcome today, see you again next time')
