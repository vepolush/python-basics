import utils


def test_process_summa():
    number_1, number_2 = [1, 2]
    expected_result = 3

    actual_result = utils.process_summa(number_1, number_2)
    assert expected_result == actual_result


def test_process_summa2():
    number_1, number_2 = [1, 6]
    expected_result = 7

    actual_result = utils.process_summa(number_1, number_2)
    assert expected_result == actual_result


def test_process_substraction2():
    number_1, number_2 = [1, 6]
    expected_result = -5

    actual_result = utils.process_substraction(subtrahend=number_1, minuend=number_2)
    assert expected_result == actual_result
