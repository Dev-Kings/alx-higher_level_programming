#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python list.
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i) {
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
