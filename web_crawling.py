
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 開啟文件,輸入資料格式
file = open("C:/Users/exe3c/Desktop/python.txt", mode="a", encoding="utf-8")
Path = Service("C:/Users/exe3c/Desktop/chromedriver.exe")
# 開啟瀏覽器
driver = webdriver.Chrome(service=Path)
# 模擬操作
chains = ActionChains(driver)
# 輸入網址
driver.get("https://www.vscinemas.com.tw/vsweb/")
# 最大化視窗
driver.maximize_window()

# 自動化操作,模擬滑鼠移動點擊
move_to_element_location1 = driver.find_element(By.XPATH , '/html/body/header/div/section/nav/ul/li[2]/a')
ActionChains(driver).move_to_element(move_to_element_location1).perform()
time.sleep(1)

move_to_element_location2 = driver.find_element(By.XPATH , '/html/body/header/div/section/nav/ul/li[2]/div/ul/li[3]/a')
ActionChains(driver).move_to_element(move_to_element_location2).perform()

# Explicit Wait
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH , '/html/body/header/div/section/nav/ul/li[2]/div/ul/li[3]/a'))
)

click_location1 = driver.find_element(By.XPATH , '/html/body/header/div/section/nav/ul/li[2]/div/ul/li[3]/a')
ActionChains(driver).click(click_location1).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH , '/html/body/article/ul/li[1]/section[2]/h2/a'))
)
time.sleep(2)
# 取得電影標題
movie_titles = driver.find_elements(By.CLASS_NAME , "infoArea")

# 將電影標題依照順序寫入文件中
i = 1
for title in movie_titles :
    file.write(str(i) + ".")
    file.write(title.text)
    file.write("\n" + "\n")
    i += 1

# 視窗滾動到底部
ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

# 自動化操作,模擬滑鼠移動點擊至下一頁面
next_page = driver.find_element(By.XPATH , '/html/body/article/section/ul/li[3]/a')
ActionChains(driver).click(next_page).perform()
time.sleep(2)
movie_titles = driver.find_elements(By.CLASS_NAME , "infoArea")

for title in movie_titles :
    file.write(str(i) + ".")
    file.write(title.text)
    file.write("\n" + "\n")
    i += 1

ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

next_page = driver.find_element(By.XPATH , '/html/body/article/section/ul/li[4]/a')
ActionChains(driver).click(next_page).perform()
time.sleep(2)
movie_titles = driver.find_elements(By.CLASS_NAME , "infoArea")

for title in movie_titles :
    file.write(str(i) + ".")
    file.write(title.text)
    file.write("\n" + "\n")
    i += 1

ScrollTO_Bottom = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(ScrollTO_Bottom)

time.sleep(2)
# 關閉瀏覽器
driver.quit()
