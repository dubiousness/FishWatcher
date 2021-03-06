from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("sender", ["sender.pyx"])]

setup(
  name = 'sender',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)


ext_modules = [Extension("receiver", ["receiver.pyx"])]

setup(
  name = 'receiver',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
