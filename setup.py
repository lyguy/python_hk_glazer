from setuptools import setup, find_packages

setup(
    name='json_to_degree',
    version='0.0.4',
    description='Convert compatible JSON configs to DeBAM/DeTIM config.dat files',
    url='https://github.com/fmuzf/meltmod_jsontodegree',
    author='Lyman Gillispie',
    author_email='lyman.gillispie@gmail.com',
    packages=find_packages(),
    scripts=['bin/js2degree'],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires = ['argparse'],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data = True
)
