from city_functions import city_country
def test_city_country():

    return_string=city_country('la','usa')
    assert  return_string=='la is in usa'