#include <pxr/usd/sdf/layer.h>
#include <pxr/usd/sdf/primSpec.h>
#include <pxr/usd/sdf/proxyTypes.h>
#include <pxr/usd/sdf/variantSetSpec.h>
#include <pxr/usd/sdf/variantSpec.h>
#include <vector>

namespace usd_utilities {
std::vector<pxr::SdfPrimSpecHandle>
iter_prim_specs(pxr::SdfPrimSpecHandle const &root) {
  std::vector<pxr::SdfPrimSpecHandle> output{};

  auto children = root->GetNameChildren();
  output.reserve(children.size() + 1);
  output.push_back(root);

  for (auto const &prim_spec : children) {
    for (auto const &variant_set : prim_spec->GetVariantSets()) {
      auto variants = variant_set.second;
      output.reserve(variants.size());

      for (auto const &data : variants) {
        auto const variant_spec = data.second;

        for (auto const &inner : iter_prim_specs(variant_spec->GetPrimSpec())) {
          output.push_back(inner);
        }
      }
    }

    for (auto const &child : iter_prim_specs(prim_spec)) {
      output.push_back(child);
    }
  }

  return output;
}

std::vector<pxr::SdfPrimSpecHandle>
iter_prim_specs(pxr::SdfLayer const &layer) {
  return iter_prim_specs(layer.GetPseudoRoot());
}
} // namespace usd_utilities
