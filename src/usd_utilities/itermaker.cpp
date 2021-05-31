#include <iterator> // std::begin / std::end
#include <pxr/base/tf/iterator.h>
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
    auto const variant_set_map = prim_spec->GetVariantSets();
    output.reserve(variant_set_map.size());

    TF_FOR_ALL(iterator, variant_set_map) {
      auto const variant_set_spec = iterator->second;

      for (auto const variant_spec : variant_set_spec->GetVariants()) {
        auto more_children = iter_prim_specs(variant_spec->GetPrimSpec());
        output.reserve(more_children.size());
        output.insert(std::end(output), std::begin(more_children),
                      std::end(more_children));
      }
    }

    auto more_children = iter_prim_specs(prim_spec);
    output.reserve(more_children.size());
    output.insert(std::end(output), std::begin(more_children),
                  std::end(more_children));
  }

  return output;
}

std::vector<pxr::SdfPrimSpecHandle>
iter_prim_specs(pxr::SdfLayer const &layer) {
  return iter_prim_specs(layer.GetPseudoRoot());
}
} // namespace usd_utilities
