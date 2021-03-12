# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:16:20 2021

@author: =GV=
"""
import datetime as dt
import modules as m


class User(object):
    id_num = 1
    types = ['normal', 'authenticator', 'admin']    # consider changing authenticator to 'organization', all users may authenticate
    def __init__(self, uName, pWord, email, uType='normal'):
        self.uName = uName
        self.pWord = pWord
        self.email = email
        self.ID = User.id_num
        self.uType = uType
        self.assets = []
        User.id_num += 1
    
    def __repr__(self):
        return f'User({repr(self.get_email())}, {repr(self.get_ID())})'
    
    def __str__(self):
        return f'ID:\t\t\t{self.get_ID()}\nusername:\t{self.get_uName()}\nemail:\t\t{self.get_email()}\n'
    
    def get_uName(self):
        return self.uName
    
    def get_pWord(self):
        return self.pWord
    
    def get_email(self):
        return self.email
    
    def get_ID(self):
        return str(self.ID).zfill(10)
    
    def get_uType(self):
        return self.uType
    
    def get_assets(self):
        return self.assets
    
    def set_uName(self, new_uName):
        try:
            assert m.is_valid_uName(new_uName) and new_uName != self.uName
            self.uName = new_uName
            return 'Username successfully changed!'
        except:
            return 'Invalid username!'
    
    def set_pWord(self, new_pWord):
        try:
            assert m.is_valid_pWord(new_pWord)
            self.pWord = new_pWord
        except:
            return 'Invalid password'
        
    def set_email(self, new_email):
        self.email = new_email
        
    def set_uType(self, new_uType):
        try:
            assert new_uType in User.types
            self.uType = new_uType
        except:
            return 'Invalid user type!'
    
    def add_asset(self, asset):
        try:
            assert m.is_valid_asset(asset) and asset not in self.assets
            self.assets.append(asset)
        except:
            return 'Invalid asset'


class Asset(object):
    index = 0
    serial_num = 0
    def __init__(self, user, prov_date):
        Asset.serial_num += 1
        self.name = None
        self.provenance_date = prov_date
        self.SN = Asset.serial_num
        self.acquisition_date = dt.datetime.date(dt.datetime.now())
        self.provenance = []        # eg. lineage of bio, or origin of art
        self.history = []
        self.owner = user.get_ID()
        self.asset_type = None
        self.index = Asset.index
        self.active_status = True        
        Asset.index += 1
        
    def __repr__(self):
        return f'Asset({repr(self.get_name())}, {repr(self.get_provenance_date())})'
    
    def __str__(self):
        return f'ID:\t\t\t{self.get_SN()}\ntype:\t\t{self.get_type()}\nname:\t\t{self.get_name()}\nprovenance date:\t{self.get_provenance_date()}'
    
    def get_name(self):
        return self.name
    
    def get_provenance_date(self):
        return dt.datetime.strftime(self.provenance_date, '%B %d, %Y')
    
    def get_SN(self):
        return 'art'+str(self.SN).zfill(10)
    
    def get_acquisition_date(self):
        return dt.datetime.strftime(self.acquisition_date, '%B %d, %Y')
    
    def get_provenance(self):
        return self.provenance
    
    def get_history(self):
        return self.history
    
    def get_owner(self):
        return self.owner
    
    def get_type(self):
        return self.asset_type
    
    def get_index(self):
        return self.index
    
    def get_active_status(self):
        return self.active_status
    
    def set_name(self, new_name):
        try:
            assert new_name != self.name and new_name != ''
            self.name = new_name
        except:
            return 'Invalid name!'
    
    def set_provenance_date(self, date):
        self.provenance_date = date
        
    def set_acquisition_date(self, date):
        self.acquisition_date = date
        
    def add_provenance(self, provenance):
        self.provenance.append(provenance)
        
    def add_history(self, previous_owner):
        self.history.append(previous_owner)
        
    def set_owner(self, owner):
        self.owner = owner.get_ID()
        
    def set_asset_type(self, asset_type):
        # assert asset_type in Asset.types
        self.asset_type = asset_type
        
    def change_active_status(self):
        if self.active_status == True:
            self.active_status = False
        else:
            self.active_status = True
   

class Biological(Asset):
    serial_num = 0
    types = ['feline']
    
    def __init__(self, user, prov_date):
        Biological.serial_num += 1
        self.name = None
        self.provenance_date = prov_date
        self.SN = Biological.serial_num
        self.acquisition_date = dt.datetime.date(dt.datetime.now())
        self.provenance = []        # eg. lineage of bio, or origin of art
        self.history = []
        self.owner = user.get_ID()
        self.asset_type = None
        self.index = Asset.index
        self.active_status = True
        Asset.index += 1

    
    def get_SN(self):
        return 'bio'+str(self.SN).zfill(10)
    
    def set_asset_type(self, asset_type):
        try:
            assert asset_type in Biological.types
            self.asset_type = asset_type
        except:
            return 'Invalid type!'

# class Exit(Exception):
#     print('Thank you for using Provenance!\n')
# test            
# new_user = User('anon', 'password', 'email@dot.com', 'admin')