from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://user.tungee.com/users/sign-in")
driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[1]/div/div/span/span/span/span[2]/input").send_keys("17802198459")
driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[2]/div/div/span/span/input").send_keys("Hgt_17802198459")
driver.find_element_by_xpath("//button[@class='ant-btn _2jejW ant-btn-primary']").click()
title=driver.title
url=driver.current_url
print(title)
print(url)