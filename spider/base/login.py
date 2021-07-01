from selenium import webdriver

def login(self,username,pwd):
    self.driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[1]/div/div/span/span/span/span[2]/input").send_keys(username)
    self.driver.find_element_by_xpath("//*[@id='user-login-wrapper']/div/div/div/section[2]/form/div[2]/div/div/span/span/input").send_keys(pwd)
    self.driver.find_element_by_xpath("//button[@class='ant-btn _2jejW ant-btn-primary']").click()