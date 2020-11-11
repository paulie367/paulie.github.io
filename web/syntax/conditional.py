user_id = input('id?')
user_pwd = input('password?')

'''
if user_input == '111111':
    print('welcome you')
else:
    print('who are you?')
'''

'''
if user_id == 'paul':
    if user_pwd == '111111':
        print('welcome you')
    else:
        print('who are you?')
else:
    print('who are you?')
'''

if user_id == 'paul' and user_pwd == '111111':
    print('welcome you')
elif user_id == 'ryan' and user_pwd == '222222':
    print('welcome you')
else:
    print('who are you?')
