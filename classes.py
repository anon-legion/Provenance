# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:16:20 2021

@author: =GV=
"""
from datetime import datetime as dt
import datetime
import modules as m


class User(object):
    id_num = 1
    types = ['normal', 'authenticator', 'admin']
    def __init__(self, uName, pWord, email, uType='normal'):
        self.uName = uName
        self.pWord = pWord
        self.email = email
        self.uID = User.id_num
        self.uType = uType
        self.assets = []
        User.id_num += 1
    
    def __repr__(self):
        return f'User({repr(self.get_email())}, {repr(self.get_uID())})'
    
    def __str__(self):
        return f'ID:\t\t\t{self.get_uID()}\nusername:\t{self.get_uName()}\nemail:\t\t{self.get_email()}\n'
    
    def get_uName(self):
        return self.uName
    
    def get_pWord(self):
        return self.pWord
    
    def get_email(self):
        return self.email
    
    def get_uID(self):
        return str(self.uID).zfill(10)
    
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
    id_num = 1
    def __init__(self, prov_date):
        self.name = None
        self.provenance_date = prov_date
        self.ID = Asset.id_num
        self.acquisition_date = dt.date(dt.now())
        self.provenance = []
        Asset.id_num += 1
        
    def __repr__(self):
        pass
    
    def __str__(self):
        pass
    
    def get_name(self):
        return self.name
    
    def get_provenance_date(self):
        return dt.strftime(self.provenance_date, '%B %d, %Y')
    
    def get_ID(self):
        return 'art'+str(self.ID).zfill(10)
    
    def get_acquisition_date(self):
        return dt.strftime(self.acquisition_date, '%B %d, %Y')
    
    def get_provenance(self):
        return self.provenance
    
    def set_name(self, name):
        try:
            assert name != self.name
            self.name = name
        except:
            return 'Invalid name!'
    
    def set_provenance_date(self, year, month, day):
        self.provenance_date = datetime.date(year, month, day)
        
    def set_acquisition_date(self, year, month, day):
        self.acquisition_date = datetime.date(year, month, day)
    
    # continue
        
# class Exit(Exception):
#     print('Thank you for using providence!\n')
# test            
# new_user = User('anon', 'password', 'email@dot.com', 'admin')