import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
import random

def initOptions(filePath):
	options = Options()

	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument("--disable-extensions")
	options.add_argument("--proxy-server='direct://'")
	options.add_argument("--proxy-bypass-list=*")
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--no-sandbox')
	options.add_argument("--mute-audio")

	options.add_argument("user-data-dir="+filePath)
	options.add_argument("--window-size=550,600")
	options.add_argument('--app=https://www.facebook.com/stories')
	return options

def initDriver(filePath):
	options = initOptions(filePath)
	driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=options)
	return driver

def auto_react(driver, react):
	list_react = {
		'like': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]',
		'love': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]',
		'thuong': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]',
		'haha': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[4]',
		'wow': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[5]'
	}
	xpath_react = list_react[react]
	xpath_go_on = '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]/div/div'
	xpath_point = '//*[@id="viewer_dialog"]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/div'
	xpath_pause = '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div[1]'
	WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath_point)))
	b1 = driver.find_element_by_xpath(xpath_point)
	b1.click()
	time.sleep(3)

	while True:
		try:
			ele = driver.find_element_by_xpath(xpath_pause)
			ele.click()
			time.sleep(3)
		except:
			pass
		a = random.randint(1,10)
		if a > 7:
			try:
				ele = driver.find_element_by_xpath(xpath_react)
				ele.click()
				time.sleep(2)
			except:
				pass
		try:
			ele = driver.find_element_by_xpath(xpath_go_on)
			ele.click()
			time.sleep(1)
		except:
			break
	return 0
		
def main(name_profile, react):
	filePath = f"{os.getcwd()}\\profiles\\{name_profile}"
	options = initOptions(filePath)
	driver = initDriver(filePath)
	title = driver.title
	print(title)
	if len(title)>20:
		time.sleep(90)
	auto_react(driver, react)
	driver.quit()

	

if __name__ == '__main__':
	check = input("Them profiles?(y): ")
	if check=='y':
		name_profile = input("Nhap ten: ")
		react = 'like'
	else:
		list_name_profile = os.listdir('profiles')
		list_react = {
			0: 'like',
			1: 'love',
			2: 'thuong',
			3: 'haha',
			4: 'wow'
		}
		print("Danh sach Profile:")
		for vt in range(len(list_name_profile)):
			print(vt,'|',list_name_profile[vt])
		print("//////////////////")
		vt = int(input("Chon profile: "))
		name_profile = list_name_profile[vt]
		print("//////////////////")
		for vt in list_react:
			print(vt,'|',list_react[vt])
		vt = int(input("Chon react: "))
		react = list_react[vt]
		print(f'Dang chay profile "{name_profile}"|"{react}"')
	main(name_profile, react)