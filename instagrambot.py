from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

title = lambda: os.system('title InstaBot v15.7.19')
title()
class msgs:
    def welcome():
        print('---====::::INSTAGRAM BOT::::====---')
        print('                                   ')
        print('                 by                ')
        print('         Matix Media, Inc.         ')
        print('                                   ')
        print('        created: 15.07.2019        ')
        print('===================================')
        print('')
        print('')

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print("IB-C:: Starte den Firefox Browser...")
        self.bot = webdriver.Firefox()
        print("IB-C:: Firefox Browser gestartet!")

    def login(self):
        bot = self.bot
        print("IB-C:: Navigiere zur Login-Page von Instagram...")
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        print("IB-C:: Erfolgreich zur Login-Page von Instagram Navigiert!")
        username_box = bot.find_element_by_name('username')
        password_box = bot.find_element_by_name('password')
        username_box.clear()
        password_box.clear()
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        print("IB-C:: Versuche Einzuloggen...")
        time.sleep(3)
        print("IB-C:: Login-Daten abgeschickt!")
    
    def gettag(self,hashtag,scrolls):
        bot = self.bot
        print("IB-C:: Navigiere zum Hashtag '#"+hashtag+"'...")
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(3)
        print("IB-C:: Erfolgreich zum Hashtag '#"+hashtag+"' Navigiert!")
        
        

    def likeImages(self,scrolls):
        done_scrolls = 0
        bot = self.bot
        print("IB-C:: Suche alle Links...")
        links = []
        for i in range(1,scrolls):
            print("IB-C:: Scrolle zum Ende der Seite (" + str(done_scrolls + 1) + " von " + str(scrolls) + " Scrolls)...")
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            print("IB-C:: Am ende der Seite!", end='\r')
            done_scrolls = done_scrolls + 1
            time.sleep(1)

            found_links = bot.find_elements_by_tag_name('a')

            for elem in found_links:
                links.append(elem.get_attribute('href'))
            #links.extend = found_links

            found_links_count = 0
            for elem in found_links:
                found_links_count = found_links_count + 1
                print("IB-C:: " + str(elem.get_attribute('href')), end='\r')

            print("IB-C:: Founded Links: " + str(found_links_count) + "                                                 ")
        time.sleep(3)

        links_count = 0
        links_used_count = 0
        links_used = []
        print("IB-C:: ALLE LINKS:")
        for elem2 in links:
            links_count = links_count + 1
            
            link_str = elem2
            if "/p/" in link_str:
                if not link_str in links_used:
                    print(link_str, end='\r')
                    links_used_count = links_used_count + 1
                    links_used.append(link_str)

        print('')
        print("IB-C:: Gefundene Links: " + str(links_count))
        print('')
        print("IB-C:: Links zu Posts: " + str(links_used_count))
        print('')
        print('')
        print("IB-C:: Beginne Links abzuarbeiten...")
        liked_posts = 0
        links_error = 0
        for link in links_used:
            print('')
            print('__________________________________________________________')
            print('IB-C:: Beitrag ' + str(liked_posts + 1) + ' von ' + str(links_used_count) + ' Beiträgen:')
            print('IB-C:: Lädt...', end='\r')
            bot.get(link)
            time.sleep(4)
            print("IB-C:: Versuche Post '" + link + "' zu Liken...")
            try:
                bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                print("IB-C:: Post '" + link + "' Erfolgreich Geliket!")
                time.sleep(1)
                liked_posts = liked_posts + 1
            except Exception as ex:
                print("IB-C:: Fehler beim Liken des Posts (Eventuell wurde der Beitrag Gelöscht oder der Link ist nicht mehr Verfügbar oder du hast diesen Beitrag schon geliked): ")
                print(ex)
                print("IB-C:: Bisherige Fehler beim Liken von " + str(liked_posts) + " Posts: " + str(links_error) + " Fehler")
                print("IB-C:: Versuche es in 30 sec beim nächsten Post erneut!", end='\r')
                time.sleep(1)
                links_error = links_error + 1
                for i in range(1,29):
                    time.sleep(1)
                    print("IB-C:: Versuche es in " + str(30 - i) + " sec beim nächsten Post erneut!", end='\r')
                    
                    
                print('')
        print('')
        clear = lambda: os.system('cls')
        clear()
        msgs.welcome()
        print(str(links_used_count - links_error) + ' von ' + str(links_used_count) + ' Beiträge erfolgreich geliked!')
        bot.get('https://www.instagram.com/'+self.username+'/')
        input("IB-C <<>>")
        bot.quit()


#clear console
clear = lambda: os.system('cls')
clear()


#welcome massage
msgs.welcome()
time.sleep(2)

#inputs
input_username = input("Ihr Benutzername: ")
print("Ihr Benutzername ist '"+input_username+"'")

print('')
input_password = input("Ihr Passwort für '"+input_username+"': ")
print("Ihr Passwort zu dem Benutzer '"+input_username+"' ist '"+input_password+"'")

print('')
print('Die 15 beliebtesten Hashtags auf Instagram (stand 15.07.2019):')
fav_hashtags = ['#love', '#instagood', '#photooftheday', '#fashion', '#beautiful', '#happy', '#cute', '#tbt', '#like4like', '#followme', '#picoftheday', '#follow', '#me', '#selfie', '#summer']
for hashtag in fav_hashtags:
    print('  ★ '+hashtag)

print('')
input_hashtag = input("Hashtag: #")
print("Ihr eingegebener Hashtag ist '#"+input_hashtag+"'")

print('')
input_scrolls = round(int(input("Zu Likende Beiträge (min. 3): ")) / 5)
print("Es werden ungefähr " + str(input_scrolls * 5) + " Beiträge geliked!")
print('')
print('')
print('Starte InstagramBot by Matix Media, Inc. ...')
time.sleep(3)
clear()

msgs.welcome()
print('')

#run code
mx = InstagramBot(input_username, input_password)

mx.login()

mx.gettag(input_hashtag, input_scrolls)

mx.likeImages(input_scrolls)