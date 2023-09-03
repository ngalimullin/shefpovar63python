import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

BASE_URL = 'https://shefpovar63.ru/'

def test_corect_send_massage(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, 'wpforms-689-field_0').send_keys('test')
    driver.find_element(By.ID, 'wpforms-689-field_1').send_keys('test@test.ru')
    driver.find_element(By.ID, 'wpforms-689-field_2').send_keys('test')
    driver.find_element(By.ID, 'wpforms-689-field_10_1').click()
    driver.find_element(By.ID, 'wpforms-689-field_10_2').click()
    driver.find_element(By.ID, 'wpforms-689-field_10_3').click()
    driver.find_element(By.ID, 'wpforms-689-field_10_5').click()
    driver.find_element(By.ID, 'wpforms-689-field_10_6').click()
    driver.find_element(By.ID, 'wpforms-689-field_11').click()
    Select(driver.find_element(By.ID, 'wpforms-689-field_11')).select_by_value('2')
    time.sleep(3)
    #driver.find_element(By.ID, 'wpforms-submit-689').click()
