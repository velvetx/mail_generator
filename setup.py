import setuptools
from distutils.core import setup
import tempfile
import shutil
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, "README.md"), encoding='utf-8') as file:
    read_me_description = file.read()

env_dir = tempfile.mkdtemp(prefix="mail_generator-install-")
shutil.copytree(os.path.abspath(os.getcwd()),
                os.path.join(env_dir, "mail_generator"))

os.chdir(env_dir)

setup(
    name='mail_generator',
    version='0.0.1',
    author='velvetx',
    platforms='GNU/Linux',
    description='A python script that generates templates..',
    long_description=read_me_description,
    long_description_content_type='text/markdown',
    url='https://github.com/velvetxq',
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3.9"],
    entry_points={
        'console_scripts': ['mail_generator = mail_generator.mail_generator:Program']
    },
    package_data={
        "mail_generator": ["*", "src/*", "logs/*", "data/*"]
    },
)
