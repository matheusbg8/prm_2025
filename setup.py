from setuptools import find_packages, setup

package_name = 'prm_2025'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='machado',
    maintainer_email='machado@todo.todo',
    description='Este pacote foi desenvolvido durante a disciplina de programação de robôs móveis',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controle_tartaruga = prm_2025.tartaruga:main',
        ],
    },
)
