#include <vector>

#include <boost/python.hpp>
#include <itermaker.h>
#include <pxr/usd/sdf/primSpec.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(itermaker) {
  def("iter_prim_specs", static_cast<std::vector<pxr::SdfPrimSpecHandle> (*)(
                             pxr::SdfPrimSpecHandle const &prim_spec)>(
                             &usd_utilities::iter_prim_specs));

  // def("iter_prim_specs",
  //     static_cast<std::vector<pxr::SdfPrimSpecHandle> (*)(
  //         pxr::Layer const &layer)>(&usd_utilities::iter_prim_specs));
}
