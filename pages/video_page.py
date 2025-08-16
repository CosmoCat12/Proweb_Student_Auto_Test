from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.course_button = (By.CSS_SELECTOR, ".home-card__top-content-list > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)")
        self.lessons_button = (By.CSS_SELECTOR, "div.tab-header__item:nth-child(2) > span:nth-child(1) > span:nth-child(1)")
        self.last_lesson_btn = (By.CSS_SELECTOR, "div.new-lessons_content-cards:nth-child(4) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)")
        self.star_btn = (By.CSS_SELECTOR, "span.baseicon:nth-child(5)")
        self.real_star_btn = (By.CSS_SELECTOR, "span.baseavatar_star:nth-child(5)")
        self.send_btn = (By.CSS_SELECTOR, "button.material-filled-button:nth-child(4) > span:nth-child(1)")
        self.play_btn = (By.CSS_SELECTOR, ".video-player-proweb__controllers-play")
        self.maximize_btn = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen")
        self.firefox_maximize_btn = (By.CSS_SELECTOR, "button.baseicon:nth-child(3)")

    def click_course_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.course_button)).click()

    def click_lessons_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.lessons_button)).click()

    def click_last_lesson_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.last_lesson_btn)).click()

    def click_star_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.star_btn)).click()

    def click_real_star_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.real_star_btn)).click()

    def click_send_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.send_btn)).click()

    def click_play_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.play_btn)).click()

    def click_maximize_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.maximize_btn)).click()

    def click_firefox_maximize_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.firefox_maximize_btn)).click()

    def click_appropriate_maximize_btn(self):
        browser_name = self.driver.capabilities.get('browserName', '').lower()
        if 'firefox' in browser_name:
            self.click_firefox_maximize_btn()
        else:
            self.click_maximize_btn()
