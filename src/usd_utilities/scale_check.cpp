#include <cmath>
#include <utility>
#include <vector>

#include <pxr/base/vt/types.h>
#include <pxr/usd/usd/attribute.h>

#include "private/common.h"
#include "scale_check.h"

static auto UPPER_BOUND = get_upper_bound();

inline static bool is_too_low(float value) {
  return std::abs(value) < UPPER_BOUND;
}

namespace usd_utilities {
Indices get_bad_scale_values(pxr::UsdAttribute const &attribute) {
  Indices output;

  pxr::VtVec3fArray values;
  attribute.Get(&values);

  for (int index = 0; index < values.size(); ++index) {
    auto value = values[index];

    if (is_too_low(value[0]) || is_too_low(value[1]) || is_too_low(value[2])) {
      output.push_back(index);
    }
  }

  return output;
}
} // namespace usd_utilities
