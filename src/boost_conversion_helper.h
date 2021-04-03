#pragma once

#include <boost/python.hpp>

using namespace boost::python;


template<typename T1, typename T2>
struct PairToPythonConverter {
    static PyObject* convert(const std::pair<T1, T2>& pair)
    {
        return incref(make_tuple(pair.first, pair.second).ptr());
    }
};

template<typename T1, typename T2>
struct PythonToPairConverter {
    PythonToPairConverter()
    {
        converter::registry::push_back(&convertible, &construct, type_id<std::pair<T1, T2> >());
    }

    static void* convertible(PyObject* obj)
    {
        if (!PyTuple_CheckExact(obj)) return 0;
        if (PyTuple_Size(obj) != 2) return 0;
        return obj;
    }

    static void construct(PyObject* obj, converter::rvalue_from_python_stage1_data* data)
    {
        tuple tuple(borrowed(obj));
        void* storage = ((converter::rvalue_from_python_storage<std::pair<T1, T2> >*) data)->storage.bytes;
        new (storage) std::pair<T1, T2>(extract<T1>(tuple[0]), extract<T2>(tuple[1]));
        data->convertible = storage;
    }
};

template<typename T1, typename T2>
struct py_pair {
    to_python_converter<std::pair<T1, T2>, PairToPythonConverter<T1, T2> > toPy;
    PythonToPairConverter<T1, T2> fromPy;
};
