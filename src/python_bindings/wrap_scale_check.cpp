#include <boost/python.hpp>
#include <pxr/usd/usd/prim.h>

#include "scale_check.h"
#include "boost_conversion_helper.h"


using namespace boost::python;


BOOST_PYTHON_MODULE(scale_check)
{
    to_python_converter< std::vector<_InstancerPair>, VecToList<_InstancerPair> >();
    py_pair<pxr::UsdPrim, _Indices>();

    def("get_bad_scale_values", usd_utilities::get_bad_scale_values);
}
