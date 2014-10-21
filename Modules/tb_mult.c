#include "Python.h"
#include "frameobject.h"
#include "opcode.h"

static 
PyObject* foo()
{
    PyThreadState *tstate = PyThreadState_GET();
    if (NULL != tstate && NULL != tstate->frame) {
        PyFrameObject *frame = tstate->frame;

        int instr = frame->f_lasti;
        unsigned char* bytes = (void*)PyString_AS_STRING(frame->f_code->co_code);
        bytes[instr + 10] = INPLACE_MULTIPLY;

    }
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef tb_mult_methods[] = {
    {"foo", (PyCFunction)foo,
        METH_NOARGS,  PyDoc_STR("")},
    {NULL, NULL} /* sentinel */
};
PyDoc_STRVAR(tb_mult_doc,"");
PyMODINIT_FUNC
inittb_mult(void)
{
    Py_InitModule3("tb_mult", tb_mult_methods, tb_mult_doc);
}
