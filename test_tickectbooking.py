from tickectbooking import calculate_average, passenger_category
def test_average_child_ages():
    ages = [5, 8, 10]
    assert calculate_average(ages) == 7.666666666666667
def test_average_adult_ages():
    ages = [25, 30, 35]
    assert calculate_average(ages) == 30
def test_average_mixed_ages():
    ages = [10, 25, 65]
    assert calculate_average(ages) == 33.333333333333336
def test_category_children():
    assert passenger_category(8) == "Children"
def test_category_adults():
    assert passenger_category(30) == "Adults"
def test_category_senior_citizens():
    assert passenger_category(65) == "Senior Citizens"
def test_average_empty_list():
    assert calculate_average([]) == 0
