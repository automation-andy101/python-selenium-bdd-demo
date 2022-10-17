from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('I launch a Chrome browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    context.driver.maximize_window()


@when('I navigate to the Orange HRM homepage')
def navigateToOrangeHrmWebsite(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(2)


@when('I enter username "{user}" and password "{pwd}"')
def enterValidCredentials(context, user, pwd):
    wait = WebDriverWait(context.driver, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))).send_keys(user)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys(pwd)
    # context.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(user)
    # context.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(pwd)
    # time.sleep(2)


@when('I click on the login button')
def clickLoginButton(context):
    context.driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()


@then('user is successfully logged in to the dashboard page')
def assertDashboardIsDisplayed(context):
    try:
        wait2 = WebDriverWait(context.driver, 2)
        empInfoText = wait2.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5'))).text

    except:
        assert False, "Test Failed!!!"
        context.driver.close()

    if empInfoText == "Employee Information":
        assert True, "Test Passed!!!"
        assert context.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
        context.driver.close()


