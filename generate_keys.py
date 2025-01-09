# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:54:02 2023

@author: burma
"""

import pickle 
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Aditya burman", "Suraj Roy", "Sushant Kumar"]
usernames = ["aburman", "sroy", "skumar"]
passwords = ["aburman", "sroy", "skumar"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)