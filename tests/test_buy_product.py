import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.courses import Courses
from pages.login_page import Login_page


def test_select_product():
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    cour = Courses(driver)
    cour.add_course()

    print("Finish test")

    time.sleep(10)
    driver.quit()
