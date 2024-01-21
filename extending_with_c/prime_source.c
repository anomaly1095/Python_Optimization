#include <Python.h>
#include <stdio.h>


// defining our module
static struct PyModuleDef prime_source = {
    PyModuleDef_HEAD_INIT,
    "__name__",
    "Custom module to find prime numbers",
    -1,
};


PyMODINIT_FUNC* PyInit_prime_shared(){
    printf("Hello from c file\n");
    return PyModule_Create(&prime_source);
}