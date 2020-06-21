from selenium import webdriver #Selenium Webdriverをインポートして
import base64
import time
import os

#mywasedaのログインIDとパス
login_id = ""
password = ""
kind = None

if login_id == "":
    login_id = input("MyWasedaのログインID:")
    password = input("MyWasedaのログインPassword:")

def main():
    login_moodle()
    open_finance_pdf()
    move_to_pdf_data()
    make_png_file()



def login_moodle():
    moodle_login = driver.find_element_by_class_name("potentialidp")
    moodle_login.click()
    mywaseda_id = driver.find_element_by_id("j_username")
    mywaseda_id.send_keys(login_id)
    mywaseda_pass = driver.find_element_by_id("j_password")
    mywaseda_pass.send_keys(password)
    mywaseda_login = driver.find_element_by_id("btn-save")
    mywaseda_login.click()
    time.sleep(3)

def open_finance_pdf():
    options = driver.find_elements_by_class_name("activityinstance")
    if kind is not None:
        options[3*kind-1].click()
    else:
        options[-2].click()
    tab_list = driver.window_handles
    driver.switch_to.window(tab_list[1])
    driver.set_window_size(940,780)


def move_to_pdf_data():
    container = driver.find_element_by_class_name("xncc-video-container")
    video = container.find_element_by_class_name("xncc-video-frame")
    src = video.get_attribute("src")
    driver.get(src)
    src = driver.find_element_by_class_name("xn-content-frame").get_attribute("src")
    driver.get(src)
    time.sleep(6)



def make_png_file():
    classes = driver.find_elements_by_class_name("page-container")

    i = 0
    for img in classes:
        i = i + 1
        string = "img_" + str(i) + ".png"
        png = img.find_element_by_class_name("canvas").screenshot_as_png
        with open("./png/"+string, "wb") as f:
            f.write(png)

if __name__ == '__main__':
    try:
        os.mkdir("png")
    except:
        print("directry is exist")
    driver = webdriver.Chrome("./chromedriver.exe") #Chromeを動かすドライバを読み込み
    driver.get("https://wsdmoodle.waseda.jp/course/view.php?id=29075#section-1") #金融工学のURL
    main()
