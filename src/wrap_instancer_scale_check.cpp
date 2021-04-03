#include <boost/python.hpp>

#include "instancer_scale_check.h"


BOOST_PYTHON_MODULE(instancer_scale_check)
{
    boost::python::to_python_converter<std::vector<int, std::allocator<int> >, VecToList<int> >();

    boost::python::def("get_bad_scale_values", usd_utilities::get_bad_scale_values);
}
