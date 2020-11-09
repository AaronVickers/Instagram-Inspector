import json
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

baseUrl = "https://www.instagram.com/"

driverOptions = Options()
driverOptions.add_argument("--log-level=3")

driver = webdriver.Chrome(options = driverOptions, service_log_path="NUL")
driver.implicitly_wait(5)
wait2 = WebDriverWait(driver, 2)

driver.get(baseUrl)

userField = driver.find_element_by_css_selector("input[name='username']")
passField = driver.find_element_by_css_selector("input[name='password']")

try:
    loginDetailsFile = open("login-details.txt", "r")
    loginDetails = loginDetailsFile.readlines()
    loginDetailsFile.close()
    
    userField.send_keys(loginDetails[0])
    passField.send_keys(loginDetails[1])
    
    loginBtn = driver.find_element_by_xpath("//button[@type='submit']")
    driver.execute_script("arguments[0].click()", loginBtn)
except:
    print("Please log in manually.")
    
    while True:
        if driver.current_url != baseUrl:
            break
        
        sleep(0.5)


try:
    wait2.until(EC.url_contains("two_factor"))
    print("Please complete the two factor authentication.")
    
    authURL = driver.current_url
    
    while True:
        if driver.current_url != authURL:
            break
        
        sleep(0.5)
except:
    pass

nonFollowers = []
notFollowing = []

pageCursor = ""
while pageCursor != None:
    driver.get(f"https://www.instagram.com/accounts/access_tool/accounts_you_follow?__a=1&cursor={pageCursor}")
    
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    pageJSON = json.loads(soup.find("body").text)
    
    for following in pageJSON["data"]["data"]:
        nonFollowers.append(following["text"])
    
    pageCursor = pageJSON["data"]["cursor"]

pageCursor = ""
while pageCursor != None:
    driver.get(f"https://www.instagram.com/accounts/access_tool/accounts_following_you?__a=1&cursor={pageCursor}")
    
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    pageJSON = json.loads(soup.find("body").text)
    
    for follower in pageJSON["data"]["data"]:
        try:
            nonFollowers.remove(follower["text"])
        except:
            notFollowing.append(follower["text"])
    
    pageCursor = pageJSON["data"]["cursor"]

nonFollowersFile = open("non-followers.txt", "w")
nonFollowersFile.write("\n".join(nonFollowers))
nonFollowersFile.close()

notFollowingFile = open("not-following.txt", "w")
notFollowingFile.write("\n".join(notFollowing))
notFollowingFile.close()

driver.quit()

while True:
    print("What would you like to do?")
    print("1. View non-followers")
    print("2. View not following")
    print("3. Exit")
    
    option = input("> ")

    try:
        option = int(option)
        
        if option == 1:
            print("\n".join(nonFollowers)+"\n")
        elif option == 2:
            print("\n".join(notFollowing)+"\n")
        elif option == 3:
            break
        else:
            print("Invalid option.")
    except:
        print("Invalid option.")
