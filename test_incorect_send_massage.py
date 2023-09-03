import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

BASE_URL = 'https://shefpovar63.ru/'

def test_incorect_send_massage(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, 'wpforms-submit-689').click()
    time.sleep(3)
    assert (driver.find_element(By.ID, 'wpforms-689-field_0-error')).text == 'Обязательное поле.'
    assert (driver.find_element(By.ID, 'wpforms-689-field_2-error')).text == 'Обязательное поле.'

def test_incorect_send_massage_email(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, 'wpforms-689-field_1').send_keys('test')
    driver.find_element(By.ID, 'wpforms-submit-689').click()
    time.sleep(3)
    assert (driver.find_element(By.ID, 'wpforms-689-field_1-error')).text == 'Введите допустимый адрес эл. почты.'