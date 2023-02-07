from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from faker import  Faker
fake = Faker()
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
actions = ActionChains(driver)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


names = [fake.unique.user_name() for i in range(4)]
fake_name=names[0]
fake_name2=names[1]
# fake_name_manager=names[2]
# fake_username_manager=names[3]



def test_creating_project():
    driver.implicitly_wait(10)
    driver.get("https://pwa.iranrahyaft.ir/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a[2]').click()
    sleep(1)
    driver.find_element("xpath","//button[text()='تشکل']").click()
    sleep(1)
    driver.find_element("id","phoneInputLogin").send_keys("09190342754")
    sleep(1)
    driver.find_element("xpath","//button[text()='ارسال کد']").click()
    sleep(1)
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[5]").send_keys("1")
    sleep(1)
    driver.find_element("xpath","//a[@href='/create']").click()
    sleep(1)
    driver.find_element("id","title").send_keys(fake_name)
    sleep(1)
    driver.find_element("xpath","//button[contains(@class,'w-5 h-5')]").click()
    sleep(1)
    driver.find_element("xpath","(//div[contains(@class,'rounded-full w-[26px]')])[2]").click()
    sleep(1)
    driver.find_element("xpath","(//button[text()='سایر'])[2]").click()
    sleep(1)
    driver.find_element("xpath","(//div[contains(@class,'rounded-full w-[26px]')])[3]").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='کتابخواني']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='ادبیات']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='تايید و ثبت موضوع']").click()
    sleep(1)
    driver.find_element("xpath","(//button[contains(@class,'w-5 h-5')])[2]").click()
    sleep(1)
    driver.find_element("xpath","//div[contains(@class,'w-[25.1px] h-[25.1px]')]").click()
    sleep(1)
    driver.find_element("xpath","//*[text()='نيازمندی خود را انتخاب کنید...']").click()
    sleep(1)
    driver.find_element('css selector', '.css-10wo9uf-option').click()
    sleep(1)
    driver.find_element("id","input").send_keys("10")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/main/div[3]/div[3]/section/section/div/div").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='تاریخ شروع']").click()
    sleep(1)
    driver.find_element("xpath","//div[text()='17']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='تاریخ پایان']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='ساعت شروع']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='ساعت پایان']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    sleep(1)
    driver.find_element("id","address").send_keys("tehran")
    sleep(1)
    driver.find_element("id","map").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='محل پروژه خود را مشخص کنید']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/main/div[9]/button").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='targetCommunity']/button").click()
    sleep(1)
    driver.find_element("xpath","//input[@type='tel']").send_keys("10")
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("18")
    sleep(1)
    driver.find_element("xpath","//button[text()='جنسیت']").click()
    sleep(1)
    driver.find_element("id","3").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(1)
    driver.find_element("id","description").send_keys("selenium")
    sleep(1)
    driver.find_element("xpath","//button[text()='ثبت پروژه']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[1]/div").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(4)
    dom = driver.page_source
    assert fake_name in dom









def test_creating_request():
    driver.implicitly_wait(10)
    driver.get("https://pwa.iranrahyaft.ir")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a[2]').click()
    sleep(1)
    driver.find_element("id","phoneInputLogin").send_keys("09155607423")
    sleep(1)
    driver.find_element("xpath","//button[text()='ارسال کد']").click()
    sleep(1)
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[3]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[4]").send_keys("1")
    driver.find_element("xpath","(//input[@type='tel'])[5]").send_keys("1")
    sleep(1)
    driver.find_element("xpath","//a[@href='/create']").click()
    sleep(1)
    driver.find_element("id","title").send_keys(fake_name2)
    sleep(1)
    driver.find_element("xpath","//button[contains(@class,'w-5 h-5')]").click()
    sleep(1)
    driver.find_element("xpath","(//div[contains(@class,'rounded-full w-[26px]')])[2]").click()
    sleep(1)
    driver.find_element("xpath","(//button[text()='سایر'])[2]").click()
    sleep(1)
    driver.find_element("xpath","(//div[contains(@class,'rounded-full w-[26px]')])[3]").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='کتابخواني']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='ادبیات']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='تايید و ثبت موضوع']").click()
    sleep(1)
    driver.find_element("xpath","(//button[contains(@class,'w-5 h-5')])[2]").click()
    sleep(1)
    driver.find_element("xpath","//div[contains(@class,'w-[25.1px] h-[25.1px]')]").click()
    sleep(1)
    driver.find_element("xpath","//*[text()='نيازمندی خود را انتخاب کنید...']").click()
    sleep(1)
    driver.find_element('css selector', '.css-10wo9uf-option').click()
    sleep(1)
    driver.find_element("id","input").send_keys("10")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/section/div[3]/div[2]/section/section/div/div").click()
    sleep(1)
    driver.find_element("css selector","input#address").send_keys("tehran")
    sleep(1)
    driver.find_element("id","map").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='محل پروژه خود را مشخص کنید']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='ثبت درخواست']").click()
    sleep(3)
    driver.find_element("xpath","//*[@id='__next']/section/div[1]/div").click()
    sleep(3)
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a[2]").click()
    sleep(3)
    driver.find_element("xpath","//a[@href='/activity']").click()
    sleep(3)
    dom = driver.page_source
    assert fake_name2 in dom



