import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        'rk4s',
        ['lib.cpp', 'main.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
        extra_compile_args=['-std=c++11'],
    ),
]

setup(
    name='rk4s',
    version='0.0.1',
    author='wheatraptor',
    description='runge-kutta 4 for systems pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11']
)