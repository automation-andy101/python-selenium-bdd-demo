from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I launch a Chrome browser')
def launchChromeBrowser(context):
    # context.driver = webdriver.Chrome()
    context.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')


@when('I navigate to the Orange HRM homepage')
def navigateToOrangeHrmWebsite(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)


@when('I enter username "{user}" and password "{pwd}"')
def enterValidCredentials(context, user, pwd):
    context.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(user)
    context.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(pwd)


@when('I click on the login button')
def clickLoginButton(context):
    context.driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()


@then('user is successfully logged in to the dashboard page')
def assertDashboardIsDisplayed(context):
    assert context.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
    time.sleep(5)

