import unittest
import os
from os.path import dirname, basename, join

from jtara1_util.serialization import GeneralSchema
from jtara1_util import setup_logger


class TestSerialization(unittest.TestCase):
    def setUp(self):
        self.logger_path = join(os.getcwd(), 'test.log')
        # if os.path.isfile(self.logger_path):
        #     os.remove(self.logger_path)

    def tearDown(self):
        pass

    def test_serialization(self):
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

    def test_logger(self):
        logger = setup_logger(self.logger_path)
        logger.info('logger msg')
        self.assertTrue(os.path.isfile(self.logger_path))


if __name__ == '__main__':
    unittest.main()
