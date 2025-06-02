from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        self.add_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        # Locators for employee details
        self.first_name_input = (By.XPATH,
                                 '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        self.last_name_input = (By.XPATH,
                                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
        self.employee_id_input = (By.XPATH,
                                  '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        self.next_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')


        self.employee_search_input = (By.XPATH,
                                      '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')

        self.search_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.pim_menu)).click()

    def click_add_employee(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_button)).click()

    def add_employee(self, first_name, last_name, employee_id):
        # Wait for first name input and fill details
        first_name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.first_name_input))
        first_name_field.send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.employee_id_input).clear()  # Clear default ID if any
        self.driver.find_element(*self.employee_id_input).send_keys(employee_id)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.next_button)).click()
        self.navigate_to_pim()

    def search_employee(self, employee_name):
        # Click on PIM tab again if needed; for simplicity, assume you are on the correct page
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.employee_search_input))
        search_input.send_keys(employee_name)
        self.driver.find_element(*self.search_button).click()