from selenium.webdriver.common.by import By

BASE_URL = 'https://shefpovar63.ru/'

def test_big_input_form_text(driver):
    driver.get(BASE_URL)
    assert (driver.find_element(By.XPATH, '//*[@data-id="e76e5b1"]/div/h2/b')).text == 'Сделаю индивидуальное предложение'

def test_smal_input_form_text(driver):
    driver.get(BASE_URL)
    assert (driver.find_element(By.CSS_SELECTOR, '.elementor-widget-container p b')).text == 'Хотите скидку 10%?'


