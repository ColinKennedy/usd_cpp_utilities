#include <vector>

#include <boost/python.hpp>
#include <pxr/usd/usd/prim.h>
#include <common.h>
#include <scale_check.h>

#include "boost_conversion_helper.h"
#include "vector_converter.h"


using namespace boost::python;


BOOST_PYTHON_MODULE(scale_check)
{
    to_python_converter< std::vector<InstancerPair>, CppVectorToPythonList<InstancerPair> >();
    py_pair<pxr::UsdAttribute, Indices>();

    def(
        "get_bad_scale_values",
        usd_utilities::get_bad_scale_values,
        R"(Find every PointInstancer Prim with small scale elements.

        Note:
            If the user's environment defines a
            USD_CPP_UTILITIES_SCALE_UPPER_BOUND variable, it is read as
            a float and used. Otherwise, 0.0001 is the fallback value.

        Args:
           range (:class:`pxr.Usd.PrimRange`):
               The Prims to check for PointInstancers and invalid scale indices.

        Returns:
           list[tuple[:class:`pxr.Usd.Attribute`, list[int]]]:
               Each PointInstancer Attribute which has 1-or-more indices
               with bad scale values.
        )"
    );
}
