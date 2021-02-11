from selenium import webdriver
from selenium.common.exceptions import *
import sys
from time import sleep
import time
import random
from selenium.webdriver.common.keys import Keys

class facebook_bot:
    def __init__(self,driver,url,username,password):
        options=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications":2}
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs",prefs)

        self.driver=webdriver.Chrome(driver,options=options)
        self.driver.get(url)    #opens the fb page
        self.login(username,password)

    def showException(self,e):
        print(e)
        self.driver.quit()
        sys.exit()

    def login(self,username,password):
        try:
            email_box=self.driver.find_element_by_id("email")
            email_box.send_keys(username)

            pass_box=self.driver.find_element_by_id("pass")
            pass_box.send_keys(password)

            login_btn=self.driver.find_element_by_xpath("//button[contains(.,'Log In')]")
            login_btn.click()
        except NoSuchElementException as e:
            self.showException(e)
        except Exception as e:
            self.showException(e)
            
    def update_status(self,message):
        sleep(1)    #used to disable notifications popup
        post_area=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span")
        post_area.click()
        sleep(2)

        active_post_area=self.driver.switch_to_active_element()
        active_post_area.send_keys(message)
        post_btn=self.driver.find_element_by_xpath("//div[@aria-label='Post'][contains(.,'Post')]")
        post_btn.click()
        sleep(4)
        print("Status updated Successfully")
        self.driver.get("https://www.facebook.com/")
        sleep(2)

    def infinte_scolling(self):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


    def comment(self,msg):
        #opening profile
        profile=self.driver.find_element_by_xpath("//a[contains(@class,'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn e72ty7fz qlfml3jp inkptoze qmr60zad btwxx1t3 tv7at329 taijpn5t k4urcfbm')]")
        profile.click()
        sleep(3)
        
        print("Viewing friends' list")
        friends=self.driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain'][contains(.,'Friends')]")
        friends.click()
        sleep(3)
        #self.infinte_scolling()

        friend_list=self.driver.find_elements_by_xpath("//div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']")
        #i=random.randrange(0,len(friend_list))
        i=0
        frnd=friend_list[i]
        frnd.click()
        sleep(3)
        print("Opened a random friend's timeline")

        select_comment_post=self.driver.find_element_by_css_selector("div[aria-label='Write a comment']")
        select_comment_post.click()
        select_comment_post.send_keys(msg)
        print("Comment written")

        select_comment_post.send_keys(Keys.ENTER)
        print("Commented successfully")
        sleep(5)
        self.driver.get("https://www.facebook.com/")
        sleep(3)
        