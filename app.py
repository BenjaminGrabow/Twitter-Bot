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
            tweetLinks = [i.get_attribute('href')
                          for i in bot.find_elements_by_xpath("//a[@dir='auto']")]  # Looking for all the element where they have an attribute dir=auto - not the best way but I was in a hurry, lol
            # now once I have all the hrefs data then I can filter them out to store only the ones with the string "status" in it
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_elements_by_xpath("//*[contains(text(), 'Follow)]").click()
                    time.sleep(20)
                except Exception as ex:
                    time.sleep(30)
                    print('FAILED')

ben = TwitterBot('username', 'password')

ben.login()
ben.follow('webdevelopment')
