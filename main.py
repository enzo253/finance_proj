import pandas 
import numpy
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

def handle_file_drop(your_file):
    file_path = your_file.data.strip()
    try:
        finance_report = pd.read_csv(file_path)
        print(finance_report.head())
            return: 'report uploaded succesfully'
    execpt Exceptions as e
    return f'unseccesfull: {e}
    
