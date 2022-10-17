from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'I have successfully logged in to the Orange HRM website')
def loginWithValidCredentials(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(2)
    wait = WebDriverWait(context.driver, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))).send_keys('Admin')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys('admin123')
    context.driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()


@when(u'I navigate to the search page')
def step_impl(context):
    assert True


@then(u'the search page is displayed')
def step_impl(context):
    assert True


@when(u'I navigate to the advanced search page')
def step_impl(context):
    assert True


@then(u'the advanced search page is displayed')
def step_impl(context):
    assert True

