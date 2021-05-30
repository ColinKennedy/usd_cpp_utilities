#include <vector>

#include <boost/python.hpp>
#include <itermaker.h>
#include <pxr/usd/sdf/primSpec.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(itermaker) {
  def("iter_prim_specs", usd_utilities::iter_prim_specs);
}
