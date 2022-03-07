# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _typemap_samples
else:
    import _typemap_samples

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def in_array1_1(arg):
    return _typemap_samples.in_array1_1(arg)

def in_array1_2(arg):
    return _typemap_samples.in_array1_2(arg)

def in_array01_1(arg):
    return _typemap_samples.in_array01_1(arg)

def in_array2_1(arg):
    return _typemap_samples.in_array2_1(arg)

def in_array2_2(arg):
    return _typemap_samples.in_array2_2(arg)

def in_array2_3(arg):
    return _typemap_samples.in_array2_3(arg)

def in_array12(arg):
    return _typemap_samples.in_array12(arg)

def in_array23(arg):
    return _typemap_samples.in_array23(arg)

def out_array1_1(start):
    return _typemap_samples.out_array1_1(start)

def out_array1_2(start, length):
    return _typemap_samples.out_array1_2(start, length)

def out_array1_malloc(start, length):
    return _typemap_samples.out_array1_malloc(start, length)

def out_array01_malloc(start, length):
    return _typemap_samples.out_array01_malloc(start, length)

def out_array2_1(start):
    return _typemap_samples.out_array2_1(start)

def out_array2_2(start, length):
    return _typemap_samples.out_array2_2(start, length)

def out_array2_3(start, length1, length2):
    return _typemap_samples.out_array2_3(start, length1, length2)

def out_array12_1(start, length1, length2):
    return _typemap_samples.out_array12_1(start, length1, length2)

def out_array23_1(start, length1, length2, length3):
    return _typemap_samples.out_array23_1(start, length1, length2, length3)

def const_string_0(string):
    return _typemap_samples.const_string_0(string)

def const_char_0(value):
    return _typemap_samples.const_char_0(value)

def inout_string(dim):
    return _typemap_samples.inout_string(dim)

def out_string(value):
    return _typemap_samples.out_string(value)

def in_strings(strings):
    return _typemap_samples.in_strings(strings)

def out_strings(length):
    return _typemap_samples.out_strings(length)

def return_string():
    return _typemap_samples.return_string()

def return_boolean(value):
    return _typemap_samples.return_boolean(value)

def return_sigerr():
    return _typemap_samples.return_sigerr()


