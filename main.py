#from apscheduler.schedulers.blocking import BlockingScheduler
import sqlite3
import pandas as pd
from package.scraper import scrapeTicker
from package.dbWriter import writeRowTicker


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import logging

import re
import sys
import time

#from PyQt5.QtWidgets import QApplication, QMessageBox

"""
def show_popup():
    app = QApplication([])  # Create the application object
    msg = QMessageBox()
    msg.setWindowTitle("Finalizado script")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()  # Show the message box
"""

activos = [['PYPL',['V','MA']],
			['KO',['PEP']],
			['VOO',[]],
			['VEA',[]],
			['VWO',[]],
			['VOOV',[]],
			['BAC',['C','JNJ','SAN']],
	]

dfFinal = pd.DataFrame(columns = ['main','PE','competidor_1','PE1','competidor_2','PE2','competidor_3','PE3'])


for a in activos:

	df1 = pd.DataFrame([[None] * 8],columns = ['main','PE','competidor_1','PE1','competidor_2','PE2','competidor_3','PE3'])

	d1 = scrapeTicker(a[0],"a")

	df1.iloc[0,0] = a[0]
	df1.iloc[0,1] = d1['pe_ratio']

	print(a[0] + ": " + d1['pe_ratio'])

	ind = 1

	for comp in a[1]:
		di = scrapeTicker(comp,"a")
		print(comp + ": " + di['pe_ratio'])
		df1.iloc[0,2*ind] = comp
		df1.iloc[0,2*ind+1] = di['pe_ratio']
		ind += 1

	dfFinal = pd.concat([dfFinal,df1],ignore_index=True)

dfFinal.to_csv("results.csv", index = False)



#show_popup()


