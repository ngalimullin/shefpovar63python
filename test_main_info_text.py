from selenium.webdriver.common.by import By

BASE_URL = 'https://shefpovar63.ru/'

def test_name_text(driver):
    driver.get(BASE_URL)
    assert (driver.find_element(By.XPATH, '//div[@data-id="74d36843"]/div/h2/b')).text == 'СЕРГЕЙ ВАСИЛЬЦОВ'
    assert (driver.find_element(By.CSS_SELECTOR, '.elementor-image-box-content .elementor-image-box-title')).text== 'Выездной шеф-повар\nСамара - Тольятти'
    #assert (driver.find_element(By.CSS_SELECTOR, '.elementor-image-box-content .elementor-image-box-title')).text == 'Самара - Тольятти'
    assert (driver.find_element(By.CSS_SELECTOR, '.elementor-image-box-content .elementor-image-box-description'))\
               .text == 'У вас скоро праздник? Нет сил и времени готовить? Все хлопоты возьмëм на себя. Приготовим и обслужим ваше мероприятие под ключ без наценки ресторана'
    assert (driver.find_element(By.XPATH, '//*[@data-id="ce691f2"]/div/h1/u')).text == 'УСЛУГИ:'