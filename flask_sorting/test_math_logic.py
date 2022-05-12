import unittest
from math_logic import LIST_OF_SORTING, get_sort


class TestLogic(unittest.TestCase):
    def test_list_of_sorting(self):
        arr = [2, 3, 56, 7, 89, 349, 3, 21]
        assert LIST_OF_SORTING['selection sort'](arr.copy()) == sorted(arr)
        assert LIST_OF_SORTING['insertion sort'](arr.copy()) == sorted(arr)
        assert LIST_OF_SORTING['heap sort'](arr.copy()) == sorted(arr)
        assert LIST_OF_SORTING['fast sort'](arr.copy(), 0, len(arr) - 1) == sorted(arr)

    def test_get_dict(self):
        list_arr = [[34, 5, 6, 7], [2, 3, 56, 7, 89, 349, 3, 21], [-345, 44, 55.6, -3, 5]]
        assert get_sort(list_arr, 'heap sort') == {
            "[-345, 44, 55.6, -3, 5]": "1.0499992640689015e-05",
            "[2, 3, 56, 7, 89, 349, 3, 21]": "1.3800003216601908e-05",
            "[34, 5, 6, 7]": "2.56"
        }
        assert get_sort(list_arr, 'insertion sort') == {
            "[-345, 44, 55.6, -3, 5]": "1.0499992640689015e-05",
            "[2, 3, 56, 7, 89, 349, 3, 21]": "1.3800003216601908e-05",
            "[34, 5, 6, 7]": "2.56"
        }
        assert get_sort(list_arr, 'selection sort') == {
            "[-345, 44, 55.6, -3, 5]": "1.0499992640689015e-05",
            "[2, 3, 56, 7, 89, 349, 3, 21]": "1.3800003216601908e-05",
            "[34, 5, 6, 7]": "2.56"
        }
        assert get_sort(list_arr, 'fast sort') == {
            "[-345, 44, 55.6, -3, 5]": "1.0499992640689015e-05",
            "[2, 3, 56, 7, 89, 349, 3, 21]": "1.3800003216601908e-05",
            "[34, 5, 6, 7]": "2.56"
        }


if __name__ == "__main__":
    unittest.main()
