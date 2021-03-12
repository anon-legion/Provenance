# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:43:53 2021

@author: =GV=
"""
import datetime as dt
import accounts



def is_valid_uName(uName):
    if len(uName) > 2 and type(uName) == str and not uName in accounts.users:
        return True
    else:
        return False
    
def is_valid_pWord(pWord):
    if input('re-enter password:\n>>> ') == pWord:
        return True
    else:
        return False
    
def is_valid_asset(asset):
    return True

def register():
    try:
        uName = input('input username:\n>>> ')
        assert len(uName) > 2 and not uName in accounts.users
        email = input('input email:\n>>> ')
        pWord = input('input password:\n>>> ')
        if is_valid_pWord(pWord):
            return (uName, pWord, email)
        else:
            raise AssertionError
    except:
        return False


def login():
        uName = input('input username:\n>>> ')
        pWord = input('input password:\n>>> ')
        return (uName, pWord)


def is_valid_day(year, month, day):
    max_day = (dt.date(year, (month + 1) % 12, 1) - dt.timedelta(days=1)).day
    if 1 <= day <= max_day:
        return True
    else:
        return False

def set_date():
    try:
        year = input('input year (yyyy):\n>>> ')
        assert year.isnumeric() and 1 < int(year) <= dt.datetime.now().year
        month = input('input month (mm):\n>>> ')
        assert month.isnumeric() and 1 <= int(month) <= 12
        day = input('input day (dd):\n>>> ')
        assert day.isnumeric()
        if is_valid_day(int(year), int(month), int(day)):
            assert dt.date(int(year), int(month), int(day)) <= dt.datetime.date(dt.datetime.now())
            return dt.date(int(year), int(month), int(day))
        else:
            raise AssertionError
    except:
        return False


def add_asset(user, asset_index):
    user.add_asset(accounts.assets[asset_index])