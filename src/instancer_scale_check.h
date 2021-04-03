#pragma once

#include <vector>

#include <boost/python.hpp>
#include <pxr/usd/usd/primRange.h>


// using _InstancerIndices = std::vector<std::pair<int, int>>;
using _InstancerIndices = std::pair<int, int>;


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
    _InstancerIndices get_bad_scale_values(pxr::UsdPrimRange range);
}
