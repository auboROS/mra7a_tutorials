from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['marker_control_python']
d['package_dir'] = {'': 'src'}
setup(**d)
