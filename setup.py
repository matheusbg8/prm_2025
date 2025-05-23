from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'prm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='machado',
    maintainer_email='matheus.m.santos@icmc.usp.br',
    description='Pacote da disciplina SSC0712: Programação de Robôs Móveis',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tartaruga = prm.controle_tartaruga:main'
        ],
    },
)
