from selenium import webdriver
from getpass import getpass

usr = input("Enter Yo Username or Email: ")
pwd = getpass("Yo Passwrord: ")

#Download and place the chrome driver.exe to a location
driver = webdriver.Chrome(executable_path=r"C:\Users\uiqbal\Desktop\chromedriver.exe")
driver.get('https://twitter.com/login')

usr_box = driver.find_element_by_class_name('js-username-field')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name('js-password-field')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector(
    'button.submit EdgeButton EdgeButton--primary EdgeButtom--medium')
login_button.submit()
