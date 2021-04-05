#include <cstdlib>
#include <vector>

#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usdGeom/pointInstancer.h>

#include "common.h"


std::vector<pxr::UsdGeomPointInstancer> _get_instancers(pxr::UsdPrimRange range)
{
    std::vector<pxr::UsdGeomPointInstancer> output;

    for (auto const &prim : range)
    {
        if (prim.IsA<pxr::UsdGeomPointInstancer>())
        {
            output.push_back(pxr::UsdGeomPointInstancer(prim));
        }
    }

    return output;
}


float _get_upper_bound()
{
    if (const char *value = std::getenv("USD_CPP_UTILITIES_SCALE_UPPER_BOUND"))
    {
        return static_cast<float>(*value);
    }

    return 0.0001f;  // The default value in case no value was defined
}
