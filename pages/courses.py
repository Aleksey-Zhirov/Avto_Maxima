import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Courses(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    courses_bat_1 = "//body//div//div//nav//div//div//div//div//div//button[1]"
    courses_bat_2 = "//html/body/div[4]/div[3]/ul/li[1]"
    add_a_course = "//button[text()='Добавить курс']"
    course_name = "//input[@id='outlined-basic']"
    beginning_of_the_course = "//form/div[1]/div/div[2]/div/div/div/div/input"
    completion_of_the_course = "//form/div[1]/div/div[3]/div/div/div/div/input"
    discipline = "//input[@id='Дисциплина']"
    teacher = "//input[@id='Преподаватель']"
    description = "//form/div[1]/div/div[6]/div/div/textarea"
    create = "//button[@type='submit']"

    # Getters

    def get_courses_bat_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.courses_bat_1)))

    def get_courses_bat_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.courses_bat_2)))

    def get_add_a_course(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_a_course)))

    def get_course_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.course_name)))

    def get_beginning_of_the_course(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.beginning_of_the_course)))

    def get_completion_of_the_course(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.completion_of_the_course)))

    def get_discipline(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discipline)))

    def get_teacher(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.teacher)))

    def get_description(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.description)))

    def get_create(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create)))

        # Actions

    def click_courses_bat_1(self):
        self.get_courses_bat_1().click()
        print("Click courses_bat_1")

    def click_courses_bat_2(self):
        self.get_courses_bat_2().click()
        print("Click courses_bat_2")

    def click_add_a_course(self):
        self.get_add_a_course().click()
        print("Click add_a_course")

    def input_course_name(self, course_name):
        self.get_course_name().send_keys(course_name)
        print("Input course_name")

    def input_beginning_of_the_course(self, beginning_of_the_course):
        self.get_beginning_of_the_course().send_keys(beginning_of_the_course)
        self.get_beginning_of_the_course().send_keys(Keys.ENTER)
        print("Input beginning_of_the_course")

    def input_completion_of_the_course(self, completion_of_the_course):
        self.get_completion_of_the_course().send_keys(completion_of_the_course)
        self.get_completion_of_the_course().send_keys(Keys.ENTER)
        print("Input completion_of_the_course")

    def click_discipline(self):
        self.get_discipline().click()
        self.get_discipline().send_keys(Keys.PAGE_DOWN)
        self.get_discipline().send_keys(Keys.ENTER)
        print("Click discipline")

    def click_teacher(self):
        self.get_teacher().click()
        self.get_teacher().send_keys(Keys.PAGE_DOWN)
        self.get_teacher().send_keys(Keys.ENTER)
        print("Click teacher")

    def input_description(self, description):
        self.get_description().send_keys(description)
        print("Input description")

    def click_create(self):
        self.get_create().click()
        print("Click create")

        # Methods

    def add_course(self):
        self.get_current_url()
        self.click_courses_bat_1()
        self.click_courses_bat_2()
        self.click_add_a_course()
        self.input_course_name("Автоматизация")
        self.input_beginning_of_the_course("27.10.2023")
        self.input_completion_of_the_course("27.11.2023")
        self.click_discipline()
        self.click_teacher()
        self.input_description("Python Selenium")
        self.click_create()
        self.driver.refresh()
        time.sleep(5)
        self.get_screenshot()
