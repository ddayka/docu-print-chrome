from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import keyboard
import time
import os

# Selenium Settings
serv = Service(r'CHROMEDRIVER FILEPATH')  # Update Filepath
options = webdriver.ChromeOptions()
options.add_argument("--allow-file-access-from-files")

# Press 'key' on keyboard, wait for duration 'sleep'
def press(key, sleep=0.1):
    keyboard.press_and_release(key)
    time.sleep(sleep)
    

# Print PDF File given FilePath, with chosen print options
def print_file(file, printer='default', copies=1, color=True, paper_size='letter', page_per_sheet=1, scale='default', custom_scale=100, two_sided=False):
    driver = webdriver.Chrome(service=serv, options=options)
    driver.get(file)
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+p')
    time.sleep(0.5)
    for x in range(5):
        press('tab')
    if printer != 'default':
        keyboard.write(printer)
        press('tab')
    press('tab')  # Method assumes you want all pages
    if copies != 1:
        keyboard.write(str(copies))
        time.sleep(0.1)
        press('tab')
    press('tab')
    if not color:
        press('up')
    press('tab')
    press('enter')
    press('tab')
    if paper_size != 'letter':
        keyboard.write(paper_size)
        time.sleep(0.1)
    press('tab')
    if page_per_sheet != 1:
        keyboard.write(str(page_per_sheet))
        time.sleep(0.1)
    press('tab')
    if scale != 'default':  # Scale should be either Fit to Paper or Fit to Printable Area
        keyboard.write(scale)
        time.sleep(0.1)
    if custom_scale != 100:
        keyboard.write('c')
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+a')
        keyboard.write(str(custom_scale))
        time.sleep(0.1)
    press('tab')
    if two_sided:
        press('enter')
        press('tab')
    press('tab')
    press('tab')
    # press('tab')  # Uncomment To Cancel Printing
    press('enter')  # Click "Print"
    time.sleep(1.0)
    driver.quit()
