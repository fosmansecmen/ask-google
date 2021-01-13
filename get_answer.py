import time, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse

class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS(executable_path='C:\\Program Files (x86)\\phantomjs-2.1.1-windows\\bin\\phantomjs')
        # self.driver = webdriver.Chrome()
        # self.driver.add_argument('headless')
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        
    def lookup(self):
        self.driver.get(self.url)
        
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'gsfi')
            ))
        except:
            print('...')
            
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        # print(str(soup))
        answer = soup.find_all(attr={"data-tts": "answers"})
        
        print(answer)
        if answer:
            answer = answer[0].get_text()
        
        self.driver.quit()
        return answer
            
            