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
        assert(expected == dict(datum))

        # deletion testing
        del datum['income']
        del expected['jtara1']['income']
        assert (dict(datum) == expected)

        # assignment testing
        datum['phone'] = 'android'
        expected['jtara1']['phone'] = 'android'
        assert (expected == dict(datum))


if __name__ == '__main__':
    t = TestSerialization()
    t.test()
