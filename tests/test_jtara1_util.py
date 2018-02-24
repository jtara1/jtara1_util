import unittest
from jtara1_util.serialization import GeneralSchema


class TestSerialization(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        datum = GeneralSchema(
            data_file='./datum_file.json', main_key='jtara1',
            name='James', major='CS', income=10, car='honda')
        print(repr(datum))
        print(datum)

        expected = {
            'jtara1': {
                'name': 'James',
                'major': 'CS',
                'income': 10,
                'car': 'honda'
            }
        }
        assert(expected == dict(iter(datum)))


if __name__ == '__main__':
    t = TestSerialization()
    t.test()
