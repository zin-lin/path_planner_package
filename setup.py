from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'path_planner_package'
nodes = 'path_planner_package/nodes'
both_tests = 'path_planner_package/nodes/both_test'
sim = 'path_planner_package/nodes/sim_only_test'
launch = 'launch'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, nodes, both_tests, sim, launch],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob(os.path.join('launch', '*launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zin',
    maintainer_email='zinlinhtun34@gmail.com',
    description='Path Planning Module for the ADS-MT system',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_planning=path_planner_package.path_planning:main'
        ],
    },
)
