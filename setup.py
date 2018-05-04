from distutils.core import setup

install_requires = {
    'json',
    'requests',
    'git+http://github.com/paulha/utility_funcs.git',
}

setup(
    name='jama_client',
    version='0.1',
    packages=['jama_client'],
    # package_dir={'': 'jama_client'},
    url='https://github.com/paulha/jama_client.git',
    license='',
    author='Paul Hanchett',
    author_email='paul.hanchett@gmail.com',
    description='JAMA Client',
    zip_safe=False
)
