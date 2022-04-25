import json
from func.operation import my_add

import pytest


def get_json():
    with open("../data/JSONDemo.json", "r") as file:
        data = json.loads(file.read())
        return list(data.values())


class TestWithJSON:
    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add_json(self, x, y, expected):
        value = my_add(int(x), int(y))
        assert value == int(expected)
