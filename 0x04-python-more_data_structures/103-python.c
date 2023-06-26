#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Prints data of the PyFloatObject.
 * @pyFloat: The PyObject representing the PyFloatObject.
 */
void print_python_float(PyObject *pyFloat)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(pyFloat))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)pyFloat)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}

/**
 * print_python_bytes - Prints data of the PyBytesObject.
 * @pyBytes: The PyObject representing the PyBytesObject.
 */
void print_python_bytes(PyObject *pyBytes)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(pyBytes))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(pyBytes);
	printf("  size: %zd\n", size);

	string = (assert(PyBytes_Check(pyBytes)), (((PyBytesObject *)(pyBytes))->ob_sval));
	printf("  trying string: %s\n", string);

	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - Prints data of the PyListObject.
 * @pyList: The PyObject representing the PyListObject.
 */
void print_python_list(PyObject *pyList)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int index = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(pyList))
	{
		size = PyList_GET_SIZE(pyList);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)pyList)->allocated);

		while (index < size)
		{
			item = PyList_GET_ITEM(pyList, index);
			printf("Element %d: %s\n", index, item->ob_type->tp_name);

			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);

			index++;
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

