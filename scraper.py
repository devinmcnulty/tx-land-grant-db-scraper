#!/usr/bin/python3

import os
import pandas as pd
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#C:\Users\devin\OneDrive\Documents\GitHub\tx-land-grant-db-scraper\pennsylvania\IEDriverServer.exe
#C:\Users\devin\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe

def navigate_to_file(input_no, fp):
     # Inintiate browser
    driver = webdriver.Firefox(firefox_profile=fp)
    #os.environ['MOZ_HEADLESS'] = '1'

    # Load browser with GLO database page
    driver.get("http://www.glo.texas.gov/history/archives/land-grants/index.cfm")

    # Find file number input field
    id_input = driver.find_element_by_name("sFileNo")

    # Clear field if something was there
    id_input.clear()
    
    # Enter file number into field
    id_input.send_keys(input_no)
    
    
    # Press RETURN, submitting form
    id_input.send_keys(Keys.RETURN)
    
    # Try to locate pdf link until page loaded            
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "landGrantPagination"))
        )
        # Find pdf
        pdf = driver.find_element_by_link_text('pdf')
        # Open pdf 
        pdf.click()
    except:
        # if not a valid file number, no pdf will be found 
        print("no pdf found")
    finally:    
        driver.close()
        
def open_file(input_no):
   fp = webdriver.FirefoxProfile()
   navigate_to_file(input_no, fp)
   
def download_file(input_no):
    mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", "/home/devin/Downloads/TX Project")
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
    fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    fp.set_preference("pdfjs.disabled", True)
    navigate_to_file(input_no, fp)
    
def get_pdf_url(input_no):
     # Inintiate browser
    display = Display(visible=0, size=[800, 600])
    display.start()
    # Set the MOZ_HEADLESS environment variable which casues Firefox to start in headless mode.
    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    # Load browser with GLO database page
    driver.get("http://www.glo.texas.gov/history/archives/land-grants/index.cfm")
    # Find file number input field
    id_input = driver.find_element_by_name("sFileNo")
    # Clear field if something was there
    id_input.clear()
    # Enter file number into field
    id_input.send_keys(input_no)
    # Press RETURN, submitting form
    id_input.send_keys(Keys.RETURN)
    # Try to locate pdf link until page loaded    
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "landGrantPagination"))
        )
        # Find pdf
        pdf = driver.find_element_by_link_text('pdf')
        # Open pdf 
        return pdf.get_attribute('href')
    except:
        # if not a valid file number, no pdf will be found 
        return "http://18.221.185.38/not_found.html"
    finally:    
        driver.close()
        
def download_files(first, last):
    # CSV file with one column of file numbers
    df = pd.read_csv("OneDrive/Documents/Work/TX Project/r10.csv")
    length = last - first
    for n in range(length):
        file_no = int(df.ix[last -n-1][0])
        print("Downloading " + str(file_no))
        download_file(file_no)
 