from selenium.webdriver.common.by import By

BASE_URL = 'https://shefpovar63.ru/'

def test_verify_main(driver):
    driver.get(BASE_URL)
    assert (driver.find_element(By.ID, 'menu-item-1276')).text == 'Главная'
    assert (driver.find_element(By.CSS_SELECTOR, '#menu-item-1510 a.menu-link')).text == 'Обо мне'
    assert (driver.find_element(By.CSS_SELECTOR, '#menu-item-1277 a.menu-link')).text == 'Контакты'

def test_verify_about_me(driver):
    driver.get(f'{BASE_URL}/?page_id=1390')
    assert (driver.find_element(By.ID, 'menu-item-1276')).text == 'Главная'
    assert (driver.find_element(By.CSS_SELECTOR, '#menu-item-1510 a.menu-link')).text == 'Обо мне'
    assert (driver.find_element(By.CSS_SELECTOR, '#menu-item-1277 a.menu-link')).text == 'Контакты'

def test_verify_contacts(driver):
    driver.get(f'{BASE_URL}/?page_id=33')
    assert (driver.find_element(By.ID, 'menu-item-1276')).text == 'Главная'
    assert (driver.find_element(By.CSS_SELECTOR, '#menu-item-1510 a.menu-link')).text == 'Обо мне'
    assert (driver.find_element(By.CSS_SELECTOR, '#menu-item-1277 a.menu-link')).text == 'Контакты'
