import os
import wget
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 開啟文件,輸入資料格式
file = open("C:/Users/user/Desktop/python.txt", mode="a", encoding="utf-8")
Path = "C:/Users/user/Desktop/chromedriver.exe"
# 開啟瀏覽器
driver = webdriver.Chrome(Path)
# 模擬操作
chains = ActionChains(driver)
# 輸入網址
driver.get("https://www.vscinemas.com.tw/vsweb/")
# 最大化視窗
driver.maximize_window()
time.sleep(1)

# 自動化操作,模擬滑鼠移動點擊
move_to_element_location1 = driver.find_element_by_xpath('/html/body/header/div/section/nav/ul/li[2]/a')
ActionChains(driver).move_to_element(move_to_element_location1).perform()
time.sleep(1)

move_to_element_location2 = driver.find_element(By.XPATH, '/html/body/header/div/section/nav/ul/li[2]/div/ul/li[3]/a')
ActionChains(driver).move_to_element(move_to_element_location2).perform()

# Explicit Wait
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/header/div/section/nav/ul/li[2]/div/ul/li[3]/a'))
)

click_location1 = driver.find_element(By.XPATH, '/html/body/header/div/section/nav/ul/li[2]/div/ul/li[3]/a')
ActionChains(driver).click(click_location1).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/article/ul/li[1]/figure/a/img'))
)

# 取得電影標題
movie_titles = driver.find_elements(By.CLASS_NAME, "infoArea")

# 將電影標題依照順序寫入文件中
i = 1
j = 1
k = 1
L = 1
for title in movie_titles:
    file.write(str(i) + ".")
    file.write(title.text)
    file.write("\n" + "\n")
    i += 1
    j += 1

# 視窗滾動到底部
ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

# 自動化操作,模擬滑鼠移動點擊至下一頁面
next_page = driver.find_element(By.XPATH, '/html/body/article/section/ul/li[3]/a')
ActionChains(driver).click(next_page).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/article/ul/li[1]/figure/a/img'))
)

movie_titles = driver.find_elements(By.CLASS_NAME, "infoArea")

for title in movie_titles:
    file.write(str(i) + ".")
    file.write(title.text)
    file.write("\n" + "\n")
    i += 1
    k += 1

ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

next_page = driver.find_element(By.XPATH, '/html/body/article/section/ul/li[4]/a')
ActionChains(driver).click(next_page).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/article/ul/li[1]/figure/a/img'))
)

movie_titles = driver.find_elements(By.CLASS_NAME, "infoArea")

for title in movie_titles:
    file.write(str(i) + ".")
    file.write(title.text)
    file.write("\n" + "\n")
    i += 1
    L += 1

ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

first_page = driver.find_element(By.XPATH, '/html/body/article/section/ul/li[2]/a')
ActionChains(driver).click(first_page).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/article/ul/li[1]/figure/a/img'))
)

# 取得電影宣傳圖
movie_pic_path = os.path.join("Movie_pictures")
os.mkdir(movie_pic_path)

i = 1
for m in range(j - 1):
    pic_name = "電影宣傳圖" + str(i) + ".jpg"
    save_as = os.path.join(movie_pic_path, pic_name)
    pics_path = "/html/body/article/ul/li[" + str(m + 1) + "]/figure/a/img"
    pics_src = driver.find_element(By.XPATH, pics_path)
    wget.download(pics_src.get_attribute("src"), save_as)
    i += 1

ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

Second_page = driver.find_element(By.XPATH, '/html/body/article/section/ul/li[3]/a')
ActionChains(driver).click(Second_page).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/article/ul/li[1]/figure/a/img'))
)

for n in range(k - 1):
    save_as = os.path.join(movie_pic_path, "電影宣傳圖" + str(i) + ".jpg")
    pics_path = "/html/body/article/ul/li[" + str(n + 1) + "]/figure/a/img"
    pics_src = driver.find_element(By.XPATH, pics_path)
    print(pics_src.get_attribute("src"))
    wget.download(pics_src.get_attribute("src"), save_as)
    i += 1

ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

Third_page = driver.find_element(By.XPATH, '/html/body/article/section/ul/li[4]/a')
ActionChains(driver).click(Third_page).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/article/ul/li[1]/figure/a/img'))
)

for o in range(L - 1):
    save_as = os.path.join(movie_pic_path, "電影宣傳圖" + str(i) + ".jpg")
    pics_path = "/html/body/article/ul/li[" + str(o + 1) + "]/figure/a/img"
    pics_src = driver.find_element(By.XPATH, pics_path)
    print(pics_src.get_attribute("src"))
    wget.download(pics_src.get_attribute("src"), save_as)
    i += 1

time.sleep(2)
# 關閉瀏覽器
driver.quit()
