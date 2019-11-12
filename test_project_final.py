import unittest
from project_final import *


root = Tk()
app = Window(root)

class Test(unittest.TestCase):

    app.combo_search.set('Last name')
    app.esearch.insert(0, 'Kaley')

    def test_search(self):

        test_array2 = [('1', 'Ram', 'Parsad', 'Ethical Hacking', 'Kathmandu', '9812345678'),
                      ('4', 'Hari', 'Bahadur', 'Ethical Hacking', 'Bhaktapur', '9898765432'),
                      ('10', 'Bikram', 'Kaley', 'Computing', 'Pokhara', '9812365421')]
        expected = [('4', 'Hari', 'Bahadur', 'Ethical Hacking', 'Bhaktapur', '9898765432')]



    abc = app.search(test_array2, '1')

    self.assertEqual(abc,expected)


    def test_sort(self):
        app.sort_combo.set('First name')
        app.sort_combo1.set('Ascending')
        test_array1 = [('1', 'Ram', 'Parsad', 'Ethical Hacking', 'Kathmandu', '9812345678'),
                      ('4', 'Hari', 'Bahadur', 'Ethical Hacking', 'Bhaktapur', '9898765432'),
                      ('10', 'Bikram', 'Kaley', 'Computing', 'Pokhara', '9812365421')]

        expected1 = [('10', 'Bikram', 'Kaley', 'Computing', 'Pokhara', '9812365421'),
                     ('4', 'Hari', 'Bahadur', 'Ethical Hacking', 'Bhaktapur', '9898765432'),
                     ('1', 'Ram', 'Parsad', 'Ethical Hacking', 'Kathmandu', '9812345678')]


        abc =app.sort(test_array1)
        self.assertEqual(abc, expected1)


if __name__ == '__main__':

    unittest.main()
