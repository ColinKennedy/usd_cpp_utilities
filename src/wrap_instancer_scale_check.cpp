#include <boost/python.hpp>

#include "instancer_scale_check.h"
#include "boost_conversion_helper.h"


using namespace boost::python;


BOOST_PYTHON_MODULE(instancer_scale_check)
{
    // TODO: Check if this is still needed
    to_python_converter<std::vector<int, std::allocator<int> >, VecToList<int> >();

    py_pair<int, int>();
    // class_<std::pair<int, int> >("IntPair")
    // .def_readwrite("first", &std::pair<int, int>::first)
    // .def_readwrite("second", &std::pair<int, int>::second);

    def("get_bad_scale_values", usd_utilities::get_bad_scale_values);
}
