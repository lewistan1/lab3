import LAB2.bmi as bmi

print("Test_bmi.py")


def test_bmi_normal_weight():
    expected_result = 0
    test_result = bmi.calculate_bmi(1.72, 65)  # Adjusted weight for normal weight
    assert expected_result == test_result

def test_bmi_over_weight():
    expected_result = 1
    test_result = bmi.calculate_bmi(1.72, 85)  # Adjusted weight for overweight
    assert expected_result == test_result

def test_bmi_under_weight():
    expected_result = -1
    test_result = bmi.calculate_bmi(1.72, 45)  # Adjusted weight for underweight
    assert expected_result == test_result