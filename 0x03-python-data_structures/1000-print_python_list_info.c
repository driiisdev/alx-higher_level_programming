#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints info about oython list
 * @p: PyPbject(python list)
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t alloc, i, j;
	struct _typeobject *type;
	PyObject *mem;
	PyListObject *pa;

	pa = (PyListObject *)p;
	i = PyList_Size(p);
	printf("[*] Size of Python List = %ld\n", i);
	alloc = pa->allocated;
	alloc = alloc;
	printf("[*] Allocated = %ld\n", alloc);
	for (j = 0; j < i; j++)
	{
		mem = PyList_GetItem(p, j);
		type = mem->ob_type;
		printf("Element %ld: %s\n", j, type->tp_name);
	}
}
