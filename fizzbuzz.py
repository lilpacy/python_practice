def fizzbuzz(params):
    if(params%3==0 and params%5==0):
        print('fizzbuzz')
    elif(params%3==0):
        print('fizz')
    elif(params%5==0):
        print('buzz')
    else:
        print(params)

params = input('値を入力してください\n')
fizzbuzz(int(params))
