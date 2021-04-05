#pragma once

#include <utility>
#include <vector>

#include <boost/python.hpp>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>


using _Indices = std::vector<int>;
using _InstancerPair = std::pair<pxr::UsdPrim, _Indices>;
using _InstancerPairs = std::vector<_InstancerPair>;


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
    /** \brief Find every PointInstancer Prim with small scale elements.
     *
     * \note
     * If the user's environment defines a
     * USD_CPP_UTILITIES_SCALE_UPPER_BOUND variable, it is read as a float
     * and used. Otherwise, 0.0001 is the fallback value.
     *
     * \return Every Prim which is a PointInstancer with at least one bad scale element.
     *
     */
    _InstancerPairs get_bad_scale_values(pxr::UsdPrimRange range);
}
