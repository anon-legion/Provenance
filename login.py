# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:17:37 2021

@author: =GV=
"""
import accounts
import classes
import main
import modules

actions = ['register', 'login', 'exit']
while action := input(f'Select and action:\n{[i for i in actions]}\n>>> ').lower():
    try:
        assert action in actions
        # register
        if action == actions[0]:
            # valid registration
            if attempt := modules.register():
                # create new user in accounts.py users dict
                accounts.users[f'{attempt[0]}'] = classes.User(*attempt)
                del(attempt)
            # invalid registration
            else:
                del(attempt)
                raise AssertionError

        # login
        if action == actions[1]:
            attempt = modules.login()
            if attempt[0] in accounts.users:
                #successful login
                if accounts.users[attempt[0]].get_pWord() == attempt[-1]:
                    print('\nlogin successful!\n')
                    main.main(accounts.users[attempt[0]])
                    break
                # invalid password
                else:
                    print('\ninvalid password!\n')
                    del(attempt)
            # invalid username
            else:
                print('username does not exist!')
                del(attempt)
                
        # exit 
        elif action == actions[-1]:
            print('\nThank you for using Provenance, good bye!\n')
            del(action)
            break
    
    except:
        print('\nInvalid!\n')
        pass
