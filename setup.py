from setuptools import setup

package_name = 'rostron_ia_ms'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, package_name +
              '/utils', package_name + '/strategies',
              package_name + '/managers'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='etienne',
    maintainer_email='contact@etienne-schmitz.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = rostron_ia_ms.main:main'
        ],
    },
)
