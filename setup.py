from distutils.core import setup

setup(
    name='csvquerytool',
    version='0.0.2',
    author='Alister Cordiner',
    author_email='alister@cordiner.net',
    packages=['csvquerytool', 'test'],
    scripts=['bin/csvquery'],
    url='http://bitbucket.org/acordiner/csvquerytool/',
    license='http://www.gnu.org/licenses/gpl.html',
    description='Execute SQL queries on CSV files.',
    long_description=open('README.txt').read(),
)
