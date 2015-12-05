import db
import unittest
import os


class SomeTest(unittest.TestCase):
    def setUp(self):
        self.path = 'db.test.pickle'
        self.data_car = "hello world!"

    def tearDown(self):
        os.remove(self.path)

    def test_save_pickle_test(self):
        self.assertFalse(os.path.exists(self.path))

        db.pickle_dump(self.path, self.data_car)

        self.assertTrue(os.path.exists(self.path))

        data_car2 = db.pickle_load(self.path)
        self.assertEqual(self.data_car, data_car2)

    def test_save_pickle_on_big_data(self):
        data = [a for a in range(30000)]
        data += ['hello {}'.format(a) for a in range(30000)]

        db.pickle_dump(self.data_car, self.path)
        data2 = db.pickle_load(self.path)
        self.assertEqual(data, data2)


if __name__ == '__main__':
    unittest.main()
