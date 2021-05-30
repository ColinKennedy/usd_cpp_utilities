#include <pxr/usd/sdf/layer.h>
#include <pxr/usd/sdf/primSpec.h>
#include <vector>

namespace usd_utilities {
std::vector<pxr::SdfPrimSpecHandle>
iter_prim_specs(pxr::SdfPrimSpecHandle const &prim_spec) {
  std::vector<pxr::SdfPrimSpecHandle> output {prim_spec};


  return output;
}

std::vector<pxr::SdfPrimSpecHandle>
iter_prim_specs(pxr::SdfLayer const &layer) {
  return iter_prim_specs(layer.GetPseudoRoot());
}
} // namespace usd_utilities
