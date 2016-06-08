import re
from robobrowser import RoboBrowser
import html2text
from bs4 import BeautifulSoup
import html5lib
from urllib.request import urlopen
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import strftime

import schedule
import time

def submit_message():

	browser = webdriver.Firefox()
	browser.implicitly_wait(10)
	browser.get('https://www.facebook.com/')
	username = browser.find_element_by_id("email")
	password = browser.find_element_by_id("pass")
	username.send_keys('firehead9742@yahoo.com')
	password.send_keys('dragon9742')
	submit = browser.find_element_by_xpath("//input[@value='Log In']")
	submit.click()
	browser.get("https://www.facebook.com/messages/janet.chen.528")
	message = browser.find_element_by_name("message_body")
	message.send_keys("")
	message.send_keys(Keys.RETURN)

def register_reminders(reminders):
	for x in reminders:
		time_string = x['Time:']
		if '-' in time_string:
			time_parts = line_data_miner(time_string, '-')
			

def shoot_reminder():
	compare_time = convert_to_minutes(strftime('%X:%M:%S'))
	for x in reminder_dict:
		time = convert_to_minutes(x['Time:'])
		if time in range(compare_time-1, compare_time+1):
			submit_message('PersonURL:', 'Message:')
			reminder_dict.remove(x)
			return
	return schedule.CancelJob		

def convert_to_minutes(normal_time):
	time_parts = line_data_miner(normal_time, ':')
	hour = time_parts[0]
	minute = time_parts[1]
	total = minute + 60 * hour
	return total


def begin_loop():
	print(1)

def boot():
	f = open('reminders.txt')
	labels = ['PersonURL:', 'Message:', 'Time:', "Frequency:"]
	reminder_dict = []
	for line in f:
		if 'PersonURL: ' in line:
			reminder_dict.append({})
		for x in labels:
			if x in line:
				reminder_dict[-1][x] = line_data_miner(line, x)[0]
	return reminder_dict

def line_data_miner(line, omit):
    return line.split(omit, 1)[1].strip(), line.split(omit, 1)[0].strip() # Splits on the colon, then strips of whitespace

if __name__ == '__main__':
	reminders = boot()
	register_reminders(reminders)
