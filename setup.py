import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

### Apps Definition ###
app_package = 'sprnt'
release_package = 'tethysapp-' + app_package
app_class = 'sprnt.app:Sprnt'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='&quot;Hydrology&quot;,&quot;Hydraulics&quot;,&quot;River Modeling&quot;,&quot;SPRNT&quot;',
    description='This app is a demonstration of the SPRNT dynamic river model. SPRNT means Simulation Program for River Networks. It uses the Saint-Venant equations to take into account the hydraulics as well as the hydrology in river modeling.',
    long_description='',
    keywords='',
    author='Ryan Egbert',
    author_email='ryanegbert12@gmail.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
