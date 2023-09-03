from selenium.webdriver.common.by import By

BASE_URL = 'https://shefpovar63.ru/'

def test_big_input_form_text(driver):
    driver.get(BASE_URL)
    assert (driver.find_element(By.CSS_SELECTOR, '.ast-custom-button-link .ast-custom-button')).text == '8 929 707 74 01'
    assert (driver.find_element(By.CSS_SELECTOR, '.elementor-button-text')).text == '8 929 707 74 01'
    driver.get(f'{BASE_URL}/?page_id=33')
    assert (driver.find_element(By.CSS_SELECTOR, '.ast-custom-button-link .ast-custom-button')).text == '8 929 707 74 01'
    assert (driver.find_element(By.CSS_SELECTOR, '.elementor-icon-list-item .elementor-icon-list-text:nth-child(2)')).text == '8 929 707 74 01'