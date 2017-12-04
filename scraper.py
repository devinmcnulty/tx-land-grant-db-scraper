import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_file(input_no, fp):
     # Inintiate browser
    driver = webdriver.Firefox(firefox_profile=fp)
    
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
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "pdf"))
        )
    finally:
        # Find pdf
        pdf = driver.find_element_by_link_text('pdf')
        # Open pdf 
        pdf.click()
        
def open_file(input_no):
   fp = webdriver.FirefoxProfile()
   navigate_to_file(input_no, fp)
   
def download_file(input_no):
    mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", "/home/devin/Downloads")
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
    fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    fp.set_preference("pdfjs.disabled", True)
    navigate_to_file(input_no, fp)
    
def get_pdf_url(input_no):
     # Inintiate browser
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
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "pdf"))
        )
    finally:
        # Find pdf
        pdf = driver.find_element_by_link_text('pdf')
        # Open pdf 
        #return pdf.get_attribute('href')
        print(pdf.get_attribute('href'))
        driver.close()

if __name__ == "__main__":
    get_pdf_url(sys.argv[1])    
