#pragma once

#include <vector>
#include <boost/python.hpp>


template<class T>
struct CppVectorToPythonList
{
    static PyObject* convert(const std::vector<T>& vec)
    {
        boost::python::list* l = new boost::python::list();

        for(size_t i = 0; i < vec.size(); i++) {
            l->append(vec[i]);
        }

        return l->ptr();
    }
};


