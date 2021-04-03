#pragma once

#include <vector>

#include <boost/python.hpp>
#include <pxr/usd/usd/primRange.h>


// TODO : Move this code elsewhere, later
template<class T>
struct VecToList
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

namespace usd_utilities
{
    std::vector<int> get_bad_scale_values(pxr::UsdPrimRange range);
}
