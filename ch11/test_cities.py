from city_functions import city_country, Employee # type: ignore

# 11.2
def test_city_country():
    formatted = city_country('raleigh', 'united states')
    assert formatted == 'Raleigh, United States'

def test_city_country_population():
    formatted = city_country('raleigh', 'united states', 20000)
    assert formatted == 'Raleigh, United States - population 20000'
