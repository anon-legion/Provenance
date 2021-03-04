# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:17:37 2021

@author: =GV=
"""
import accounts
import classes
import main
import modules

while True:
    actions = ['register', 'login', 'exit']
    print('\nSelect and action:')
    for i in actions:
        print(i)
    action = input('What would you like to do?\n').lower()
    try:
        assert action in actions
        if action == actions[0]:        # register
            attempt = modules.register()
            if attempt == False:        # invalid registration
                del(attempt)
                raise AssertionError
            else:                       # valid registration
                accounts.users[f'{attempt[0]}'] = classes.User(*attempt)    # create new user in accounts.py users dict
                del(attempt)
        
        if action == actions[1]:        # login
            attempt = modules.login()
            if attempt[0] in accounts.users:
                if accounts.users[attempt[0]].get_pWord() == attempt[-1]:   #successful login
                    print('\nlogin successful!\n')
                    main.main(accounts.users[attempt[0]])
                    break
                else:                   # invalid password
                    print('\ninvalid password!\n')
                    del(attempt)            
            else:                       # invalid username
                print('username does not exist!')
                del(attempt)
                                    
        elif action == actions[-1]:     # exit 
            print('\nThank you for using providence, good bye!\n')
            break
    
    except:
        print('\nInvalid!\n')
        pass
