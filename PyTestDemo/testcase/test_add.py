import openpyxl as openpyxl
import pytest
from func.operation import my_add


def get_excel():
    book = openpyxl.load_workbook("../data/params.xlsx")

    sheet = book.active

    cells = sheet["A1":"C3"]
    print(cells)
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values


class TestWithExcel:
    @pytest.mark.parametrize('x,y,expected', get_excel(), ids=["1", "2", "3"])
    def test_add(self, x: object, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
