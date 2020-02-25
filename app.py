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
        for i in range(1, 1000):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[contains(@data-testid, 'follow')]").click()
                    time.sleep(15)
                except Exception as ex:
                    print('FAILED')
                    time.sleep(30)

ben = TwitterBot('YourUsername', 'YourPassword') # change it to your username and password

ben.login()
ben.follow('webdevelopment') # change this to whatever hashtag you want to 
