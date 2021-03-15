# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:49:54 2021

@author: =GV=
"""
import accounts
import classes
import modules as m

user_types = classes.User.get_types(classes.User)[:]  # ['normal', 'authenticator', 'admin']

def normal(user):
    # print('in user console')
    actions = ['manage assets', 'exit']
    while (action := input(f'Select an action:\n{[action for action in actions]}\n>>> ').lower()) != actions[-1]:        
        try:
            assert action in actions
            # manage_assets
            if action == actions[0]:
                asset_actions = ['add', 'exit']
                while (action := input(f'Select an action:\n{[action for action in asset_actions]}\n>>> ').lower()) != asset_actions[-1]:
                    try:
                        assert action in asset_actions
                        # manage_assets/add
                        if action == asset_actions[0]:
                            print('\nSet date of provenance:')
                            date = m.set_date()
                            # invalid date
                            if date == False:
                                del(attempt)
                                raise AssertionError
                            # valid date
                            else:
                                # created asset is stored in asset vault
                                accounts.assets.append(attempt := classes.Biological(user, date))
                                # asset is added to owners assets from asset vault
                                m.add_asset(user, attempt.get_index())
                                del(date, attempt)
 
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
        