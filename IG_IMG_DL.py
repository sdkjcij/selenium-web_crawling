import os
import wget
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:/Users/user/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(1)

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
)
login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))
)
# username.clear()
# password.clear()
username.send_keys('_aries0329_')
password.send_keys('Cc1195887@@')
ActionChains(driver).click(login).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div'))
)

search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div')
ActionChains(driver).move_to_element(search).perform()
ActionChains(driver).click(search).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'))
)

search_form = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
ActionChains(driver).move_to_element(search_form).perform()
ActionChains(driver).click(search_form).perform()

keyword = input()
search_form.send_keys("#"+str(keyword))
time.sleep(1)
search_form.send_keys(Keys.RETURN)
time.sleep(1)
search_form.send_keys(Keys.RETURN)
time.sleep(10)

# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[3]/a/div/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[2]/div[1]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[2]/div[2]/a/div/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[2]/div[3]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[3]/div[3]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[4]/div[1]/a/div/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[8]/div[3]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[10]/div[1]/a/div[1]/div[1]/img
# /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[12]/div[3]/a/div/div[1]/img

# imgs = driver.find_elements(By.XPATH, 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')
path = os.path.join(keyword)
os.mkdir(path)

# count = 0
# for img in imgs:
#     save_as = os.path.join(path, keyword + str(count) + '.jpg')
#     print(img.get_attribute("src"))
#     wget.download(img.get_attribute("src"), save_as)
#     count += 1
for i in range(1, 10):
    ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(ScrollTO_Bottom)
    for j in range(1, 4):
        for k in range(1, 4):
            if (j + 4*(i-1)) > 3:
                save_as = os.path.join(path, keyword + str(j + 4 * (i - 1)) + "-" + str(k) + ".jpg")
                imgs_path = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div/div[" + str(j + 4 * (i - 1)) + "]/div[" + str(k) + "]/a/div[1]/div[1]/img"
                imgs_src = driver.find_element(By.XPATH, imgs_path)
                print(imgs_src.get_attribute("src"))
                wget.download(imgs_src.get_attribute("src"), save_as)

            else:
                save_as = os.path.join(path, keyword + str(j + 4*(i-1)) + "-" + str(k) + ".jpg")
                imgs_path = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[" + str(j + 4*(i-1)) + "]/div[" + str(k) + "]/a/div[1]/div[1]/img"
                imgs_src = driver.find_element(By.XPATH, imgs_path)
                print(imgs_src.get_attribute("src"))
                wget.download(imgs_src.get_attribute("src"), save_as)

