from selenium.webdriver.common.by import By

BASE_URL = 'https://shefpovar63.ru/'

def test_open_page(driver):
    driver.get(BASE_URL)
    assert 'shefpovar63' in driver.current_url
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1510 a.menu-link').click()
    assert '/?page_id=1390' in driver.current_url
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1276 a.menu-link').click()
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1277 a.menu-link').click()
    assert '?page_id=33' in driver.current_url

def verify_about_me(driver):
    driver.get(f'{BASE_URL}/?page_id=1390')
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1276 a.menu-link').click()
    assert 'https://shefpovar63.ru/' in driver.current_url
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1510 a.menu-link').click()
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1277 a.menu-link').click()
    assert '?page_id=33' in driver.current_url

def verify_contacts(driver):
    driver.get(f'{BASE_URL}/?page_id=33')
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1276 a.menu-link').click()
    assert 'https://shefpovar63.ru/' in driver.current_url
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1277 a.menu-link').click()
    driver.find_element(By.CSS_SELECTOR, '#menu-item-1510 a.menu-link').click()
    assert '/?page_id=1390' in driver.current_url