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
while (action := input(f'Select an action:\n{[action for action in actions]}\n>>> ').lower()) != actions[-1]:
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
        elif action == actions[1]:
            # successful login
            if (attempt := modules.login())[0] in accounts.users and accounts.users[attempt[0]].get_pWord() == attempt[-1]:
                print('\nLogin successful!\n')
                main.main(accounts.users[attempt[0]])
                break                
            # invalid login
            else:
                print('Invalid login!')
                del(attempt)
    
    except:
        print('\nInvalid!\n')
        pass

print('\nThank you for using Provenance, good bye!\n')
del(action)