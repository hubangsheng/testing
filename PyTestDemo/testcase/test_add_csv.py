import csv

import pytest
from func.operation import my_add


def get_csv():
    with open("../data/CSVDemo.csv", "r") as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    return data


class TestWithCSV:
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_add_csv(self, x, y, expected: object):
        assert my_add(int(x), int(y)) == int(expected)
