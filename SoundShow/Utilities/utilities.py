# This will be used for usefull functions like
# hashing and password strength
import hashlib
import os
import string


def hash_password(password):
    '''return sha256 hash of password'''
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def valid_username(user_name):
    '''Each username should be at least 6 characters long, will convert
    all to lowercase when entered, should also have at least number
    also no special characters'''
    if len(user_name) < 6:
        return False
    digit_count = 0
    for char in user_name:
        if char in string.punctuation:
            return False
        if char.isdigit():
            digit_count += 1
    return digit_count  # If its anything other then 0 it will be true, if 0 its false


def valid_password(pass_word):
    '''Passwords should be between 8 and 12 characters long.
    Should have at least one uppercase one number and one special 
    character in the set (!,$,@,#, &)
    '''
    if len(pass_word) > 12 or len(pass_word) < 8:
        return False
    special_chars = {'!', '@', '#', '$', '&'}
    upper = 0
    digit = 0
    special = 0
    for chars in pass_word:
        if chars in string.ascii_uppercase:
            upper += 1
        elif chars in string.digits:
            digit += 1
        elif chars in special_chars:
            special += 1
    return upper and digit and special