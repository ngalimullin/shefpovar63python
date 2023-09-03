BASE_URL = 'https://shefpovar63.ru/'

def test_titel(driver):
    driver.get(BASE_URL)
    assert driver.title == 'Кейтеринг, Выездной повар, Доставка еды в Самаре'

def test_abaut_me_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=1390')
    assert driver.title == 'Сергей Васильцов'

def test_acontacts_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=33')
    assert driver.title == 'Шеф повар +7 929 707 74 01'

def test_banket_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=583')
    assert driver.title == 'Выездной банкет в Самаре'

def test_barbeku_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=806')
    assert driver.title == 'Выездной шашлычник в Самаре'

def test_corparation_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=817')
    assert driver.title == 'Повар на корпоратив, доставка еды в офис'

def test_delivery_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=1186')
    assert driver.title == 'Доставка еды, Доставка готовых блюд, Доставка обедов'


def test_buffet_me_titel(driver):
    driver.get(f'{BASE_URL}/?page_id=1210')
    assert driver.title == 'Выездной фуршет в Самаре'

def tesy_master_clas(driver):
    driver.get(f'{BASE_URL}/?page_id=1230')
    assert driver.title == 'Кулинарный мастер класс Самара'




