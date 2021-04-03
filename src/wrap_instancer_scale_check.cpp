#include <boost/python.hpp>

#include "instancer_scale_check.h"
#include "boost_conversion_helper.h"


using namespace boost::python;


BOOST_PYTHON_MODULE(instancer_scale_check)
{
    // TODO: Check if this is still needed
    to_python_converter<std::vector<_InstancerPair, std::allocator<_InstancerPair> >, VecToList<_InstancerPair> >();

    def("get_bad_scale_values", usd_utilities::get_bad_scale_values);
}
