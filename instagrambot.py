from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        username_box = bot.find_element_by_name('username')
        password_box = bot.find_element_by_name('password')
        username_box.clear()
        password_box.clear()
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        time.sleep(3)

    # def follow(self,hashtag):


fav_hashtags = ['#love', '#instagood', '#photooftheday', '#fashion', '#beautiful', '#happy',
                '#cute', '#tbt', '#like4like', '#followme', '#picoftheday', '#follow', '#me', '#selfie', '#summer']
ben = InstagramBot('username', 'password')

ben.follow('code')
