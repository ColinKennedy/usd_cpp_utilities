#include <pxr/usd/sdf/layer.h>
#include <pxr/usd/sdf/primSpec.h>
#include <vector>

/**
 * \namespace usd_utilities
 * \brief All public objects in this Rez package which external packages may
 * use.
 */
namespace usd_utilities {
std::vector<pxr::SdfPrimSpecHandle>
iter_prim_specs(pxr::SdfPrimSpecHandle const &prim_spec);

std::vector<pxr::SdfPrimSpecHandle> iter_prim_specs(pxr::SdfLayer const &layer);
} // namespace usd_utilities
