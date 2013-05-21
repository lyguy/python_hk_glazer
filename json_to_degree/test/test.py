from nose.tools import with_setup
import os
import json_to_degree as jtodeg
import subprocess


class TestClass:

  @classmethod
  def setup_class(cls):
    cls.here = os.path.dirname(__file__)
    cls.data =  cls.here + '/data'

  def test_1(self):
      '''Test 1: Check that json_to_degree works when imported'''
      jtodeg.json_to_dat(self.data
          + "/json_test_in.json", output="test1.txt"
          , silent=True)
      with open("test1.txt") as file:
          gen_str = file.read()
      with open(self.data + "/json_test_out.txt") as file:
          test_str = file.read()

      assert(test_str == gen_str)
      os.remove("test1.txt")
      pass      


  def test_2(self):
      '''Test 2: Check command line execution'''
      cmd = os.path.abspath(self.here + '/../../bin/js2degree.py')
      print(cmd)
      subprocess.call([cmd, self.data + "/json_test_in.json", "-o=test2.txt", "-s"])
      with open("test2.txt") as file:
          gen_str = file.read()
      with open(self.data + "/json_test_out.txt") as file:
          test_str = file.read()

      assert(test_str == gen_str)
      os.remove("test2.txt")
      pass
