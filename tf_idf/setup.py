


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import os
import Cython.Compiler.Options

import shutil


Cython.Compiler.Options.annotate = True
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'

tf_idf_cy = Extension('cy_tf_idf',
                sources=[ROOT_DIR + 'cy_tf_idf.pyx'],
                extra_compile_args=["-std=c++11", "-Ofast",  "-ftree-vectorize", "-msse2"],
                extra_link_args=["-std=c++11", "-Ofast",  "-ftree-vectorize", "-msse2"],
                include_dirs=[ROOT_DIR, '.'],
                language='c++')

modules = [tf_idf_cy]


for e in modules:
    e.cython_directives = {'language_level': "3"}

setup(
    name='cy_tokenizer_interface',
    ext_modules=modules,
    cmdclass={'build_ext': build_ext},
    script_args=['build_ext'],
    options={'build_ext': {'inplace': True, 'force': True}},
)