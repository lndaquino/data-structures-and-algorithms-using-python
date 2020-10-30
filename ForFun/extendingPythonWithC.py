#python .\extendingPythonWithC.py build #executar na linha de comando para criar o módulo e depois usar
from distutils.core import setup, Extension

module = Extension('fib', sources = ['fibonacci.c'])
setup(name = 'PackageName', version = '1.0', description = 'Pacote para o módulo', ext_modules = [module])