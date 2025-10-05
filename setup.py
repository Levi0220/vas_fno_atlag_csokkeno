from setuptools import setup

package_name = 'vas_fno_atlag_csokkeno'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/array.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Levi',
    maintainer_email='levente.vass@ddc.sze.hu',
    description='Array publisher + descending sorter + averager + range.',
    license='GNU General Public License v3.0',
    entry_points={
        'console_scripts': [
            'array_publisher = vas_fno_atlag_csokkeno.array_publisher:main',
            'array_sorter    = vas_fno_atlag_csokkeno.array_sorter:main',
            'array_averager  = vas_fno_atlag_csokkeno.array_averager:main',
            'array_range     = vas_fno_atlag_csokkeno.array_range:main',
        ],
    },
)