from tkinter import * 
import tkinter as tk
import time;
from tkinter import Tk, PhotoImage, messagebox, ttk
r1 = open("gebruiker1.txt", "r").readlines()[10]; w=r1.strip()
w += '1'
print(w)
