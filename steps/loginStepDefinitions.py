from behave import *
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


@given(u'I visit the Sauce Demo website login page')
def navigateToSauceDemoWebsite(context):
    # context.driver=webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')


@when(u'I enter valid login credentials')
def submitValidLoginCredentials(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID, 'login-button').click()


@then(u'I should see the inventory page')
def assertHomePageIsDisplayed(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'


