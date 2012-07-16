import os

def test_1():
    '''Test 1: Check that json_to_degree works when imported'''
    import json_to_degree as jtodeg
    jtodeg.jsontodat("test/json_test_in.json", output="foo.txt", silent=True)
    with open("foo.txt") as file:
        gen_str = file.read()
    os.remove("foo.txt")

    with open("test/json_test_out.txt") as file:
        test_str = file.read()

    assert(test_str == gen_str)

def test_2():
    '''Test 2: Check command line execution'''
    import subprocess
    subprocess.call(["./json_to_degree.py","test/json_test_in.json", "-o=foo.txt", "-s"])
    with open("foo.txt") as file:
        gen_str = file.read()
    os.remove("foo.txt")
    with open("test/json_test_out.txt") as file:
        test_str = file.read()

    assert(test_str == gen_str)
    pass
