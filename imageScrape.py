import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

def main():
    #*------------------------------------------------------------------
    # item_list = [
    #     "french+fries",
    # ]
    # varient = {
    #     "stock+photos" : 90,
    #     "front+view" : 90,
    #     "kfc" : 20,
    #     "macdonald" : 20,
    #     "cheese" : 20,
    #     "potato" : 50,
    #     "with+ketchup" : 50
    # } 
    # item_list = [
    #     "เฟรนฟราย",
    #     "เฟรนฟรายชีสดิป"
    #     "เฟรนฟรายชีส"
    #     "เฟรนฟรายชีสเยิ้ม"
    # ]
    # varient = {
    #     "" : 20
    # }
    #*------------------------------------------------------------------
    # item_list = [
    #     "ผัดซีอิ๊วเส้นใหญ่หมูใส่ไข่",
    # ]
    # varient = {
    #     "stock+photos" : 90,
    #     "front+view" : 50,
    #     "" : 90,
    #     "ชัด": 90,
    #     "7-11": 90
    # } 
    #*------------------------------------------------------------------
    # item_list = [
    #     "ข้าวหมกไก่"
    # ]
    # varient = {
    #     "" : 90,
    # } 
    item_list = [
        "Chicken Biryani"
    ]
    varient = {
        "stock+photos" : 90,
        "front+view" : 90,
        "" : 90,
        "hd images": 50
    } 

    folder_path = 'image/Chicken Biryani' + '/' #* Change your destination path here
    image_scrape(item_list, varient, folder_path)
        

def image_scrape(item_list, varient, folder_path):
    driver_path = 'chromedriver'  #* Replace with the actual path to the downloaded driver
    counter = 0
    for item_model in item_list:
        for model_option, numOfPics in varient.items():
            options = webdriver.ChromeOptions()
            options.add_argument('--user-data-dir=/Users/a970/Library/Application Support/Google/Chrome/Default')
            options.add_argument('--headless')
            driver = uc.Chrome(options=options)
            if model_option == "":
                url = str(f"https://www.google.com/search?q={item_model}&hl=en&tbm=isch&sxsrf=APwXEdeMCCcn15mo1obWv-xVcr_tpnFYQg%3A1684476865544&source=hp&biw=1737&bih=1032&ei=wRNnZNX-HtX4kPIP9umT2AY&iflsig=AOEireoAAAAAZGch0VXQnHgSIAIKBwcg5h0gf-nJjQvD&oq=toyota+supr&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgQIIxAnMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6CAgAELEDEIMBOgQIABADOgkIABAYEIAEEApQlglY7SNgpSxoB3AAeAGAAZIBiAHkDJIBBDEwLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img")
            else:
                url = str(f"https://www.google.com/search?q={item_model}+{model_option}&hl=en&tbm=isch&sxsrf=APwXEdeMCCcn15mo1obWv-xVcr_tpnFYQg%3A1684476865544&source=hp&biw=1737&bih=1032&ei=wRNnZNX-HtX4kPIP9umT2AY&iflsig=AOEireoAAAAAZGch0VXQnHgSIAIKBwcg5h0gf-nJjQvD&oq=toyota+supr&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgQIIxAnMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6CAgAELEDEIMBOgQIABADOgkIABAYEIAEEApQlglY7SNgpSxoB3AAeAGAAZIBiAHkDJIBBDEwLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img")
            driver.get(url)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(4)
            if (numOfPics > 50):
                for i in range(0, 3):
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    time.sleep(2)
            elif (numOfPics > 20):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)
            img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")
            image_urls = []
            for img in img_results:
                image_urls.append(img.get_attribute('src'))
            modifiedName = item_model.replace("+", " ")
            for i in range(numOfPics):
                counter += 1
                urllib.request.urlretrieve(str(image_urls[i]), folder_path + "{0} {1}.jpg".format(modifiedName, counter))
            driver.quit()
        counter = 0

main()