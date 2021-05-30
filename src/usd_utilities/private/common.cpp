#include <cstdlib>
#include <vector>

#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usdGeom/pointInstancer.h>

#include "common.h"

float get_upper_bound() {
  if (const char *value = std::getenv("USD_CPP_UTILITIES_SCALE_UPPER_BOUND")) {
    return static_cast<float>(*value);
  }

  return 0.0001f; // The default value in case no value was defined
}
