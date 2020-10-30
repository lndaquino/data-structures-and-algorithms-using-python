#include "C:\Python37\include\Python.h"

/*
flag de compilação: -IC:\ (somente para windows) - não precisou
PY Py
o tipo PyObject é sempre usado como ponteiro
Exemplo: static PyObject* myfunc(PyObject* self)
Exemplo de função do Python.h
PyArg_ParseTuple(args, format..)
structure PyMethodDef
{NULL, NULL, 0, NULL}
static PyMethodDef myMethods[] = {
  {"func1", func1, METH_NOARGS, "func1 docs"},
  {...}
  {NULL, NULL, 0, NULL}
}
*/

/*
Sequencia de Fibonacci
1,1,2,3,5,8
*/
int fib(int n)
{
  if(n < 2)
    return n;
  return fib(n-1) + fib(n-2)
}

static PyObject* fib(PyObject* self, PyObject* args)
{
  int n;
  if(!PyArg_ParseTuple(args, "i", &n))
    return NULL;

  return Py_BuildValue("i", Cfib(n));
}

static PyObject* version(PyObject* self)
{
  return Py_BuildValue("s", "Versão 1.0");
}

static PyMethodDef myMethods[] = {
  {"fib", fib, METH_VARARGS, "Cálculo do número de Fibonacci"},
  {"version", version, METH_NOARGS, "Retorna a versão"},
  {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initmyModule(void)
{
  (void) Py_InitModule("fib", myMethods)
}