from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class AutoTinder():

    def __init__(self, email, password):
        self.password = password
        self.email = email
        self.browser = webdriver.Chrome()

    def connect(self):
        self.browser.maximize_window()
        self.browser.get('https://tinder.com/app/recs')
        self.browser.implicitly_wait(10)

    def login(self, email, password):
        cookies_accept = self.browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookies_accept.click()

        login_click = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_click.click()

        time.sleep(2)
        facebook_connexion = self.browser.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        facebook_connexion.click()
        time.sleep(2)
        base_window = self.browser.window_handles[0]
        pop_up = self.browser.switch_to_window(self.browser.window_handles[1])

        time.sleep(1)
        number_input = self.browser.find_element_by_xpath('//*[@id="email"]')
        number_input.send_keys(email)



        time.sleep(1)
        password_input = self.browser.find_element_by_xpath('//*[@id="pass"]')
        password_input.send_keys(password)

        time.sleep(1)
        connect_button = self.browser.find_element_by_xpath('//*[@id="u_0_0"]')
        connect_button.click()

        self.browser.switch_to_window(base_window)

    def auth_location_notification(self):
        time.sleep(1)
        autorise_location_btn = self.browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        autorise_location_btn.click()

        time.sleep(1)
        notification_btn = self.browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification_btn.click()

    def close_pop(self):
        pop = self.browser.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[1]')
        pop.click()

    def like(self):
        like_btn = self.browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def auto_like(self):
        while True:
            time.sleep(0.5)
            try:
                self.like()
            except Exception:
                self.close_pop()

    def tinder(self):
        self.connect()
        self.login(self.email, self.password)
        self.auth_location_notification()
        self.auto_like()

