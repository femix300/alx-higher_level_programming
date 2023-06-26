#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list
 * @p: PyObject representing the Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);

	PyObject *item;
	Py_ssize_t i;

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: PyObject representing the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);
	char *string = PyBytes_AsString(p);
	Py_ssize_t i;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	printf("  trying string: %s\n", string);

	printf("  first %zd bytes:", (size < 10) ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02hhx", string[i]);
	}
	printf("\n");
}

