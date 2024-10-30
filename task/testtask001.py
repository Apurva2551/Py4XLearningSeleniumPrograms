import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Make Appointment Url Verification")
@allure.description("By clicking on MAke appointment we are verifying the url and sign in and again verifying the url after signin")


def test_make_appointment_verify_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment=driver.find_element(By.LINK_TEXT,"Make Appointment")
    make_appointment.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    password=driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    login= driver.find_element(By.ID,"btn-login")
    login.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

