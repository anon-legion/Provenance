# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:49:54 2021

@author: =GV=
"""
import accounts
import classes
import modules as m

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
            # manage_assets
            if action == actions[0]:
                asset_actions = ['add', 'exit']
                while True:
                    print('\nManage assets\nSelect an action:')
                    for i in asset_actions:
                        print(i)
                    action = input('What would you like to do?\n').lower()
                    assert action in asset_actions
                    try:
                        # manage_assets/add
                        if action == asset_actions[0]:
                            print('\nSet date of provenance:')
                            date = m.set_date()
                            # invalid asset
                            if date == False:
                                del(attempt)
                                raise AssertionError
                            # valid asset
                            else:
                                attempt = classes.Biological(user, date)
                                accounts.assets.append(attempt)
                                m.add_asset(user, attempt.get_index())
                                del(date, attempt)
                                # assets not adding, check add_asset module
                        
                        # manage_assets/exit
                        elif action == asset_actions[-1]:
                            break
                    except:
                        pass
                    
            elif action == actions[-1]:         # exit
                print('\nThank you for using Provenance, good bye!\n')
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
        