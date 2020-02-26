from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(3)

        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def follow(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23' +
                hashtag + '&src=typed_query')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[not(contains(@data-testid,'unfollow')) and contains(@data-testid, 'follow')]").click()
                    time.sleep(15)
                except Exception as ex:
                    print('FAILED')
                    time.sleep(2)
    
    def like(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23' +
                hashtag + '&src=typed_query')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[not(contains(@data-testid,'unfollow')) and contains(@data-testid, 'follow')]").click()
                    time.sleep(15)
                except Exception as ex:
                    print('FAILED')
                    time.sleep(2)

ben = TwitterBot('username', 'password')

ben.login()

ben.follow('code')

time.sleep(300)
ben.follow('coding')


time.sleep(600)
ben.follow('react')


time.sleep(900)
ben.follow('reactnative')


time.sleep(1200)
ben.follow('github')


time.sleep(1500)
ben.follow('opensource')

time.sleep(1800)
ben.follow('computerscience')


time.sleep(2100)
ben.follow('webdevelopment')


time.sleep(2400)
ben.follow('lambdaschool')

time.sleep(2700)
ben.follow('algorithm')

time.sleep(3000)
ben.follow('algorithm')

time.sleep(3300)
ben.follow('software')