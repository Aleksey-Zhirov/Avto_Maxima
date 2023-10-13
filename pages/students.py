import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Student(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)

        # Locators

    student_bat_1 = "//body//div//div//nav//div//div//div//div//div//button[2]"
    student_bat_2 = "//html/body/div[4]/div[3]/ul/li[1]"
    add_student = "//*[@id='root']/div[1]/div/div[1]/div/button[1]"
    login_name = "//input[@name='login']"
    last_name = "//input[@name='lastName']"
    first_name = "//input[@name='firstName']"
    email = "//input[@name='email']"
    date_birth = "//form/div/div/div[11]/div/div/div/div/input"
    create = "//button[@type='submit']"
    search_student = "//input[@name='Поиск ученика']"

    # Getters

    def get_student_bat_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.student_bat_1)))

    def get_student_bat_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.student_bat_2)))

    def get_add_student(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_student)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_date_birth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_birth)))

    def get_create(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create)))

    def get_search_student(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_student)))

        # Actions

    def click_student_bat_1(self):
        self.get_student_bat_1().click()
        print("Click student_bat_1")

    def click_student_bat_2(self):
        self.get_student_bat_2().click()
        print("Click student_bat_2")

    def click_add_student(self):
        self.get_add_student().click()
        print("Click add_student")

    def input_login_name(self, login_name):
        self.get_login_name().send_keys(login_name)
        print("Input login_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_date_birth(self, date_birth):
        self.get_date_birth().send_keys(date_birth)
        self.get_date_birth().send_keys(Keys.ENTER)
        print("Input date_birth")

    def click_create(self):
        self.get_create().click()
        print("Click create")

    def input_search_student(self, search_student):
        self.get_search_student().send_keys(search_student)
        print("Click search_student")

        # Methods

    def add_students(self):
        self.get_current_url()
        self.click_student_bat_1()
        self.click_student_bat_2()
        self.click_add_student()
        self.input_login_name("1One_student")
        self.input_email("1one_student@email.com")
        self.input_last_name("1Студентов")
        self.input_first_name("1Студент")
        self.input_date_birth("04.02.1985")
        self.click_create()
        self.input_search_student("1Студ")
        time.sleep(5)
        self.get_screenshot()
