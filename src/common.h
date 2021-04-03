#pragma once

#include <vector>

#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usdGeom/pointInstancer.h>


std::vector<pxr::UsdGeomPointInstancer> _get_instancers(pxr::UsdPrimRange range);

float _get_upper_bound();
