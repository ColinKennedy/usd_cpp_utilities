#include <cstdlib>
#include <string>

#include "common.h"

float get_upper_bound() {
  const char *value = std::getenv("USD_CPP_UTILITIES_SCALE_UPPER_BOUND");

  if (!value)
  {
    return 0.0001f; // An arbitrary default value in case no value was defined
  }

  return std::stof(value);
}
