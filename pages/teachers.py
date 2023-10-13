import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Teacher(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    teacher_bat_1 = "//body//div//div//nav//div//div//div//div//div//button[2]"
    teacher_bat_2 = "//html/body/div[3]/div[3]/ul/li[2]"
    add_a_teacher = "//button[text()='Добавить преподавателя']"
    login_name = "//input[@name='login']"
    last_name = "//input[@name='lastName']"
    first_name = "//input[@name='firstName']"
    email = "//input[@name='email']"
    create = "//button[@type='submit']"
    search_teacher = "//input[@name='Поиск']"

    # Getters

    def get_teacher_bat_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.teacher_bat_1)))

    def get_teacher_bat_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.teacher_bat_2)))

    def get_add_a_teacher(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_a_teacher)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_create(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create)))

    def get_search_teacher(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_teacher)))

        # Actions

    def click_teacher_bat_1(self):
        self.get_teacher_bat_1().click()
        print("Click teacher_bat_1")

    def click_teacher_bat_2(self):
        self.get_teacher_bat_2().click()
        print("Click teacher_bat_2")

    def click_add_a_teacher(self):
        self.get_add_a_teacher().click()
        print("Click add_a_teacher")

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

    def click_create(self):
        self.get_create().click()
        print("Click create")

    def input_search_teacher(self, search_teacher):
        self.get_search_teacher().send_keys(search_teacher)
        print("Click search_teacher")

        # Methods

    def add_teacher(self):
        self.get_current_url()
        self.click_teacher_bat_1()
        self.click_teacher_bat_2()
        self.click_add_a_teacher()
        self.input_login_name("1One_teacher")
        self.input_last_name("1Анкудинов")
        self.input_first_name("1Александр")
        self.input_email("1one_teacher@email.com")
        self.click_create()
        self.input_search_teacher("1Анкудин")
        time.sleep(5)
        self.get_screenshot()
