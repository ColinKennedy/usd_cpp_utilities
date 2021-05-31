#include <vector>

#include <boost/python.hpp>
#include <itermaker.h>
#include <pxr/usd/sdf/layer.h>
#include <pxr/usd/sdf/primSpec.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(itermaker) {
  def("iter_prim_specs",
      static_cast<std::vector<pxr::SdfPrimSpecHandle> (*)(
          pxr::SdfPrimSpecHandle const &prim_spec)>(
          &usd_utilities::iter_prim_specs),
      R"(Get every PrimSpec on and under `prim_spec`.

      This function is inclusive. The first yielded value will be `prim_spec`.

      Args:
          prim_spec (:class:`pxr.Sdf.PrimSpec`): The PrimSpec to find children from.

      Returns:
          list[:class:`pxr.Sdf.PrimSpec`]: `prim_spec` + all of its children, if any.

      )");

  def("iter_prim_specs",
      static_cast<std::vector<pxr::SdfPrimSpecHandle> (*)(
          pxr::SdfLayer const &layer)>(&usd_utilities::iter_prim_specs),
      R"(Get every PrimSpec on and under some Sdf Layer.

      This function is inclusive. The pseudo-root of `layer` is the first
      PrimSpec yielded.

      Args:
          root (:class:`pxr.Sdf.Layer`): The Layer to get all content of.

      Returns:
          list[:class:`pxr.Sdf.PrimSpec`]: `root` + all of its children, if any.

      )");
}
