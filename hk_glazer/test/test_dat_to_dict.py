from nose.tools import with_setup
import os
import hk_glazer as js2deg
import subprocess
import json
import collections

def convert(data):
    if isinstance(data, unicode):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


class TestClass:

  @classmethod
  def setup_class(cls):
    cls.here = os.path.dirname(__file__)
    cls.data =  cls.here + '/data'

  def test_dat_to_dict_file(self):
    '''Test reading input.txt as file'''
      
    with open(self.data + "/json_test_out.txt") as f:
      test_dict = js2deg.input_to_dict(f)

    with open(self.data + "/json_test_in.json") as f:
      verif_dict = convert(json.load(f))

    assert(test_dict == verif_dict)
    pass      

  
  def test_dat_to_dict_string(self):
    '''Test reading input.txt as string'''
      
    with open(self.data + "/json_test_out.txt") as f:
      s = f.read()
      test_dict = js2deg.input_to_dicts(s)

    with open(self.data + "/json_test_in.json") as f:
      verif_dict = convert(json.load(f))

    assert(test_dict == verif_dict)
    pass      


  def test_dat_to_dict_cli(self):
    cmd = os.path.abspath(self.here + '/../../bin/hk_glazer')
    subprocess.check_call([cmd, "degree2js", self.data + "/json_test_out.txt", "-o=test2.json", "-s"])
    with open("test2.json") as f:
        gen_dict = convert(json.load(f))

    with open(self.data + "/json_test_in.json") as f:
        test_dict = convert(json.load(f))

    assert(test_dict == gen_dict)
    os.remove("test2.json")
    pass



