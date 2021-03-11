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
    while (action := input(f'Select and action:\n{[i for i in actions]}\n>>> ').lower()) != actions[-1]:        
        try:
            assert action in actions
            # manage_assets
            if action == actions[0]:
                asset_actions = ['add', 'exit']
                while (action := input(f'Select and action:\n{[i for i in asset_actions]}\n>>> ').lower()) != asset_actions[-1]:
                    try:
                        assert action in asset_actions
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
 
                    except:
                        print('\nInvalid Asset action!')
                  
        except:
            print('\nInvalid')
            
        del(action)

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
        