
#include "oled.h"
#include "pytohn.h" 

static PyObject * oled_init(PyObject * self, int chnl, int addr, int type, int flip, int inv)
{
	oledInit(chnl,addr,type,flip,inv);
	return Py_None;
};

static PyObject * oled_shutdown(PyObject * self)
{
	oledShutdown();
	return Py_None;
};

static PyObject * oled_writeString(PyObject * self, int x, int y, char * var, int size)
{
	oledWriteString(x, y, var, size);
	return Py_None;
};


static PyObject * oled_drawLine(PyObject *self, int x1, int y1, int x2, int y2, unsigned char pix)
{
	oledDrawLine(x1, y1, x2, y2, pix);
	return Py_None;
};

static struct PyMethodDef dd_oled_methods[] = 
{
	{"init",(PyCFunction)oled_init, METH_VARARGS, "Display GPIO intialization"},
	{"shutdown", (PyCFunction)oled_shutdown, METH_NOARGS, "shut down display"},
	{"write_string", (PyCFunction) oled_writeString, METH_VARARGS, "Display text on screen"},
	{"draw_line", (PyCFunction) oled_drawLine, METH_VARARGS, "Draw a line between two points on screen"}
};

static struct PyModuleDef dd_oled_module = {
	PyModuleDef_HEAD_INIT,
	"dd_oled",
	"Python interface for the oled module",
	-1,
	dd_oled_methods
};

PyMODINIT_FUNC PyInit_dd_oled(void) {
	return PyModule_Create(&dd_oled_module);
};