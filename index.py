from mimetypes import init
from pyclbr import Class
import array as arr
from numpy import array 
import requests as axios # only by habit =)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from bs4 import BeautifulSoup as bs

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)

# test selenium driver with instagram login/navigate
class InstagramClass:
    ROUTES = {'home': 'instagram.com'}
    def __init__(self, driver) -> None:
        self.goTo()
        pass
    def login(self):
        user = input('Nome de usuário: ')
        password = input('Senha: ')
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm input[name='username']")))
        userField = driver.find_element(By.CSS_SELECTOR, "#loginForm input[name='username']")
        passField = driver.find_element(By.CSS_SELECTOR, "#loginForm input[name='password']")
        userField.send_keys(user)
        passField.send_keys(password)
        passField.send_keys(Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html.logged-in a[href='/direct/inbox/']")))
    def goTo(self, path = 'home'):
        url = 'https://' + self.ROUTES[path]
        #print(url)
        driver.get(url)

insta = InstagramClass(driver)
insta.login()
insta.goTo()
#driver.quit();
quit()