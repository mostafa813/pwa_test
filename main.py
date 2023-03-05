from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from faker import  Faker
fake = Faker()
from selenium.webdriver.remote.webelement import WebElement
from random import randint

random_number = randint(100000000000000000000000,999999999999999999999999)
print(random_number)


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
actions = ActionChains(driver)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.alert import Alert
alert = Alert(driver)
names = [fake.unique.user_name() for i in range(4)]
fake_name=names[0]
fake_name2=names[1]
# fake_name_manager=names[2]
# fake_username_manager=names[3]



def test_creating_project():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","(//input[@id='title'])[2]").send_keys("tehran")
    sleep(1)
    driver.find_element("xpath","//*[@id='map']").click()
    sleep(1)
    driver.find_element("xpath","/html/body/div[1]/section/main/div[5]/section/section/div[3]/button").click()
    sleep(1)
    driver.find_element("id","description").send_keys("selenium")
    sleep(1)
    driver.find_element("xpath","(//button[contains(@class,'w-5 h-5')])[2]").click()
    sleep(1)
    driver.find_element("css selector","div#subject>p").click()
    sleep(1)
    driver.find_element("css selector","button[class$='items-center']").click()
    sleep(1)
    driver.find_element('css selector', "div[id='requirementSelect']").click()
    sleep(1)
    driver.find_element('css selector', '.css-10wo9uf-option').click()
    sleep(1)
    driver.find_element("id","input").send_keys("10")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='createP']/main/div[8]/section/div[2]/div[3]/section/section/div/div").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='تاریخ شروع']").click()
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
    driver.find_element("css selector","div[class$='text-eminence']").click()
    sleep(1)
    driver.find_element("xpath","(//input[@id='title'])[3]").send_keys("عنوان خدمت")
    driver.find_element("id","react-select-requirementSelect-placeholder").click()
    driver.find_element("css selector","div[id='react-select-requirementSelect-option-0']").click()
    driver.find_element("xpath","(//input[@placeholder='بنویسید'])[3]").click()
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    driver.find_element("xpath","(//input[@placeholder='بنویسید'])[4]").click()
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    driver.find_element("xpath","(//input[@placeholder='مثال : تهران ، شهرک شهید خرازی ، برج  شهید باقری'])[2]").send_keys("tehran")
    driver.find_element("xpath","(//button[@id='map'])[2]").click()
    driver.find_element("xpath","(//button[text()='محل پروژه خود را مشخص کنید'])[2]").click()
    driver.find_element("xpath","(//textarea[@id='description'])[2]").send_keys("توضیحات خدمت")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید و ادامه']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='ثبت پروژه']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[1]/div").click()
    sleep(1)
    driver.find_element("css selector","svg[width='22']").click()
    sleep(3)
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(4)
    dom = driver.page_source
    assert fake_name in dom







def test_creating_request():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","(//input[@id='title'])[2]").send_keys("tehran")
    sleep(1)
    driver.find_element("id","map").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='محل پروژه خود را مشخص کنید']").click()
    sleep(1)
    driver.find_element("id","description").send_keys("selenium")
    sleep(1)
    driver.find_element("css selector","div#__next>section>section>div:nth-of-type(6)>button").click()
    sleep(1)
    driver.find_element("xpath","//p[contains(@class,'text-[14px] font-normal')]").click()
    sleep(1)
    driver.find_element("xpath","(//div[contains(@class,'rounded-full w-[26px]')])[3]").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='کتابخواني']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='ادبیات']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='تايید و ثبت موضوع']").click()
    sleep(1)
    driver.find_element("xpath","//p[contains(@class,'text-[14px] font-normal')]").click()
    sleep(1)
    driver.find_element("xpath","//button[contains(@class,'fixed bottom-14')]").click()
    sleep(1)
    driver.find_element("xpath","//div[text()='نيازمندی خود را انتخاب کنید...']").click()
    sleep(1)
    driver.find_element('css selector', '.css-10wo9uf-option').click()
    sleep(1)
    driver.find_element("id","input").send_keys("10")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/section/div[7]/div[2]/div[2]/section/section/div/div").click()
    sleep(1)
    driver.find_element("id","calendar").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='انتخاب']").click()
    sleep(1)
    driver.find_element("id","clock").click()
    sleep(1)
    driver.find_element("xpath", "//button[text()='انتخاب']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='ثبت درخواست']").click()
    sleep(3)
    # driver.find_element("xpath","//*[@id='__next']/section/div[1]/div").click()
    # sleep(3)
    # driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a[2]").click()
    # sleep(3)
    # driver.find_element("xpath","//a[@href='/activity']").click()
    # sleep(3)
    # dom = driver.page_source
    # assert fake_name2 in dom





def test_requesting_acces_to_profile():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(1)
    driver.find_element("xpath","//div[text()='درخواست ها']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/main/div[1]/section/div[4]/a/button").click()
    sleep(2)
    driver.find_element("xpath","//button[text()='درخواست دسترسی به پروفایل']").click()
    sleep(1)
    driver.find_element("xpath","//div[text()='بنویسید']").click()
    sleep(1)
    driver.find_element("xpath","//*[text()='معیشتی']").click()
    sleep(1)
    driver.find_element("xpath","//textarea[@placeholder='بنویسید']").send_keys("test")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(3)
    dom = driver.page_source
    assert 'در انتظار تایید کاربر' in dom




def test_accept_the_acces_to_profile():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(3)
    driver.find_element("xpath","//button[text()='مدیریت کنش ها']").click()
    sleep(2)
    # driver.find_element("xpath","//div[@id='__next']/section[1]/div[51]/section[1]/div[4]/a[1]/button[1]").click()
    # sleep(3)
    # driver.find_element("xpath","//span[text()='تشكل هاي درخواستی']").click()
    # sleep(1)
    # driver.find_element("xpath","//button[text()='مشاهده دسترسی ها']").click()
    # sleep(1)
    # driver.find_element("xpath","//button[text()='تایید درخواست']").click()
    # sleep(2)
    # dom = driver.page_source
    # assert 'تایید دسترسی' in dom





def test_creating_proposal():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
    sleep(2)
    driver.find_element("xpath","//button[text()='مدیریت کنش ها']").click()
    sleep(1)
    driver.find_element("xpath","//div[@id='__next']/section[1]/div[13]/section[1]/div[4]/a[1]/button[1]").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='درخواست تنفیذ ( ایجاد پروژه)']").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='تاریخ شروع']").click()
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
    driver.find_element("xpath","//div[contains(@class,'relative bg-biloba_40')]//button[1]").click()
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
    sleep(3)
    dom = driver.page_source
    assert 'در انتظار تایید کاربر' in dom








def test_aprove_proposal():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
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
    sleep(3)
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a[2]").click()
    sleep(3)
    driver.find_element("xpath","//button[text()='مدیریت کنش ها']").click()
    sleep(1)
    driver.find_element("xpath","//div[@id='__next']/section[1]/div[51]/section[1]/div[4]/a[1]/button[1]").click()
    sleep(1)
    driver.find_element("xpath","//span[text()='تشكل هاي درخواستی']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='مشاهده پیشنهاد']").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید پیشنهاد']").click()
    sleep(2)
    dom = driver.page_source
    assert 'مشاهده پروژه متناظر' in dom






def test_chat_by_tashakol():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/button").click()
    sleep(1)
    driver.find_element("xpath","//div[@class='flex mx-3']").click()
    sleep(4)
    driver.find_element("xpath","//textarea[@placeholder='بنویسید']").send_keys("test of selenium")
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[2]/div[2]/button").click()
    sleep(4)







def test_edit_profile_by_person():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[1]/div[2]").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='ویرایش پروفایل']").click()
    sleep(1)
    driver.find_element("xpath","//input[@id='title']").send_keys("مصطفی کاشی")
    driver.find_element("xpath","(//input[@id='title'])[2]").click()
    sleep(1)
    driver.find_element("xpath","(//button[text()='تایید'])[2]").click()
    sleep(1)
    driver.find_element("xpath","//input[@placeholder='مثال : تهران ، شهرک شهید خرازی ، برج  شهید باقری']").send_keys("تهران")
    sleep(1)
    driver.find_element("css selector","button#map>div>div").click()
    sleep(1)
    driver.find_element("xpath","//button[text()='محل پروژه خود را مشخص کنید']").click()
    sleep(1)
    driver.find_element("id","description").send_keys("سلام")
    sleep(1)
    driver.find_element("xpath","//button[text()='تایید']").click()
    sleep(3)







def test_coment_in_project_by_person():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/main/div[1]/section/a").click()
    sleep(2)
    driver.find_element("id","description").send_keys(fake_name)
    sleep(1)
    driver.find_element("xpath","//button[text()='ارسال']").click()
    sleep(3)
    dom = driver.page_source
    assert fake_name in dom










def test_coment_in_tashakol_profile_by_person():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(1)
    driver.find_element("xpath","//div[text()='تشکل ها']").click()
    sleep(1)
    driver.find_element("xpath","")


    driver.find_element("id","description").send_keys(fake_name)
    sleep(1)
    driver.find_element("xpath","//button[text()='ارسال']").click()
    sleep(3)
    dom = driver.page_source
    assert fake_name in dom







def test_coment_in_project_by_tashakol():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
    sleep(1)
    driver.find_element("xpath", "//button[text()='تشکل']").click()
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
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/main/div[1]/section/a").click()
    sleep(1)
    driver.find_element("id","description").send_keys(fake_name)
    sleep(1)
    driver.find_element("xpath","//button[text()='ارسال']").click()
    sleep(3)
    dom = driver.page_source
    assert fake_name in dom






def test_coment_in_tashakol_profile_by_tashakol():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath", "//button[text()='لیست']").click()
    sleep(1)


    driver.find_element("id","description").send_keys(fake_name)
    sleep(1)
    driver.find_element("xpath","//button[text()='ارسال']").click()
    sleep(3)
    dom = driver.page_source
    assert fake_name in dom







def test_add_shaba_number_by_tashakol():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div/div[2]").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='کیف پول']").click()
    sleep(1)
    driver.find_element("xpath","//h5[text()='حساب ها (شبا)']").click()
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(1)
    driver.find_element("tag name","input").send_keys(random_number)
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(3)
    dom = driver.page_source
    assert str(random_number) in dom







def test_delet_shaba_number_by_tashakol():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div/div[2]").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='کیف پول']").click()
    sleep(1)
    driver.find_element("xpath","//h5[text()='حساب ها (شبا)']").click()
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(1)
    driver.find_element("tag name","input").send_keys(random_number)
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[2]/div[1]/div/div[2]/div[2]").click()
    sleep(3)
    dom = driver.page_source
    assert str(random_number)  not in dom









def test_add_money_to_wallet_by_tashakol():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app/")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div/div[2]").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='کیف پول']").click()
    sleep(1)
    driver.find_element("xpath","//h5[text()='افزایش اعتبار']").click()
    sleep(1)
    driver.find_element("tag name","input").send_keys("100")
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(2)
    driver.find_element("xpath","//input[@value='پرداخت موفق']").click()
    sleep(4)







def test_add_shaba_number_by_person():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div/div[2]").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='کیف پول']").click()
    sleep(1)
    driver.find_element("xpath","//h5[text()='حساب ها (شبا)']").click()
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(1)
    driver.find_element("tag name","input").send_keys(random_number)
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(3)
    dom = driver.page_source
    assert str(random_number) in dom







def test_delet_shaba_number_by_person():
    driver.implicitly_wait(10)
    driver.get("https://dev-pwa.hnaya.app")
    driver.set_window_size(360,800)
    sleep(1)
    driver.find_element("xpath",'//*[@id="__next"]/section/div[4]/section/div[3]/a').click()
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
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div/div[2]").click()
    sleep(1)
    driver.find_element("xpath","//p[text()='کیف پول']").click()
    sleep(1)
    driver.find_element("xpath","//h5[text()='حساب ها (شبا)']").click()
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(1)
    driver.find_element("tag name","input").send_keys(random_number)
    sleep(1)
    driver.find_element("tag name","button").click()
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[2]/div[1]/div/div[2]/div[2]").click()
    sleep(3)
    dom = driver.page_source
    assert str(random_number)  not in dom


test_delet_shaba_number_by_person()

