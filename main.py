# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:49:54 2021

@author: =GV=
"""
import classes

user_types = classes.User.types[:]  # ['normal', 'authenticator', 'admin']

def normal(user):
    # print('in user console')
    actions = ['manage assets', 'exit']
    while True:
        print('\nSelect an action:')
        for i in actions:
            print(i)
        action = input('What would you like to do?\n').lower()
        try:
            assert action in actions
            if action == actions[0]:            # manage_assets
                actons = ['add', 'exit']
                while True:
                    print('\nManage assets\nSelect an action:')
                    for i in action:
                        print(i)
                    action = input('What would you like to do?\n').lower()
                    assert action in actions
                    try:
                        if action == actions[0]:    # manage_assets/add
                            attempt = classes.Asset()
                        
                        elif action == actions[-1]: # manage_assets/exit
                            break
                    except:
                        pass
                    
            elif action == actions[-1]:         # exit
                print('\nThank you for using providence, good bye!\n')
                break
        except:
            pass

def main(user):
    if user.get_uType() == user_types[0]:       # normal
        print(user)
        normal(user)
    elif user.get_uType() == user_types[1]:     # authenticator
        pass
    elif user.get_uType() == user_types[-1]:    # admin
        pass
    else:                                       # unregistered browsing
        pass
        