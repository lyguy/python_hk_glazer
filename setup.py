from setuptools import setup, find_packages

setup(
    name='hk_glazer',
    version='0.0.8-0.0.1',
    description='Convert compatible JSON configs to DeBAM/DeTIM config.dat files',
    url='https://github.com/fmuzf/python_hk_glazer',
    author='Lyman Gillispie',
    author_email='lyman.gillispie@gmail.com',
    packages=find_packages(),
    scripts=['bin/hk_glazer'],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires = ['argparse'],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data = True
)
