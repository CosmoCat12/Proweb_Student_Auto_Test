from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_button = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar")
        self.exit_button = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(8) > div > div > div.list-tile__title-box > h3")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")

    def click_profile_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_button)).click()

    def click_exit_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_button)).click()

    def click_confirm_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.confirm_exit)).click()
