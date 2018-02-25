import json
import os
import dill
import collections
from pprint import pformat


class Serialization:
    def __init__(self, data_file):
        self.data_file = os.path.abspath(data_file)
        self.data = {}

    @staticmethod
    def make_paths_for_file(file_path, is_file=True):
        """Make folders if needed for data file"""
        path = os.path.dirname(file_path) \
            if is_file else os.path.abspath(file_path)
        if not os.path.exists(path):
            os.makedirs(path)

    def serialize_as_json(self):
        Serialization.make_paths_for_file(self.data_file)
        json.dump(obj=self.data, fp=open(self.data_file, 'w'))

    def deserialize_from_json(self, default=None):
        try:
            self.data = json.load(fp=open(self.data_file, 'r'))
            return self
        except (FileExistsError, FileNotFoundError):
            print('[Serialization] WARNING: {} not found,\n'
                  '\treturned default value: {}'.format(self.data_file, default))
            return default

    def serialize_as_binary(self):
        Serialization.make_paths_for_file(self.data_file)
        dill.dump(obj=self.data, file=open(self.data_file, 'wb'))

    def deserialize_from_binary(self, default=None):
        try:
            self.data = dill.load(file=open(self.data_file, 'rb'))
            return self
        except (FileExistsError, FileNotFoundError):
            print('[Serialization] WARNING: {} not found,\n'
                  '\treturned default value: {}'.format(self.data_file, default))
            return default


class GeneralSchema(Serialization, collections.MutableMapping):
    def __init__(self, data_file, main_key, **kwargs):
        """General Schema (like an abstract class)
        Creates something like this:

        .. code-block:: python
        md = GeneralSchema('~/app.config', 'app_name', version='0.1.0',
                           'search-engine'='google.com')
        assert(dict(md) == \
        {'app_name': {
            'version': '0.1.0',
            'search-engine': 'google.com'
            }
        })

        end e.g.. Where 'video.mp4' is the main key and its value are kwargs
        """
        Serialization.__init__(self, data_file)
        self.main_key = main_key
        self.data[main_key] = {}

        self.data[main_key].update(kwargs)

    serialize = Serialization.serialize_as_json  # alias, new ref
    deserialize = Serialization.deserialize_from_json  # alias, new ref

    def __iter__(self):
        """Convert this instance to a dictionary. Only yielding keys"""
        for key in self.data.keys():
            yield key

    def __getitem__(self, key):
        """Square brackets operator overriding. e.g.: datum['main_key']
        :param key: key used to find a value in self.data
        :return: a value from self.data or self.data[self.main_key] \n
            or self.main_key
        """
        # same as using the dot operator to access main_key attr
        if key == 'main_key':
            return self.main_key

        # return the actual datum
        elif key == self.main_key:
            return self.data[self.main_key]

        # return {main_key: datum} where datum is dictionary
        return self.data[self.main_key][key]

    def __setitem__(self, key, value):
        if key == 'main_key':
            self.main_key = value
        elif key == self.main_key:
            self.data[self.main_key] = value
        else:
            self.data[self.main_key][key] = value

    def __delitem__(self, key):
        # same as using the dot operator to access main_key attr
        if key == 'main_key' or key == self.main_key:
            self.data.clear()
            self.main_key = None

        # return {main_key: datum} where datum is dictionary
        else:
            del self.data[self.main_key][key]

    def __len__(self):
        return len(self.data['main_key'].keys())

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self)

    def __repr__(self):
        """:return: string of dictionary of all public attributes"""
        return str(self.__dict__)

    def __str__(self):
        """:return: string of self.data (same as dict(self))"""
        return str(dict(self))


if __name__ == '__main__':
    pass
