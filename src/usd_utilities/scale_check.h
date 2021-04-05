#pragma once

#include <utility>
#include <vector>

#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>


using _Indices = std::vector<int>;
using _InstancerPair = std::pair<pxr::UsdPrim, _Indices>;
using _InstancerPairs = std::vector<_InstancerPair>;


namespace usd_utilities
{
    /** \brief Find every PointInstancer Prim with small scale elements.
     *
     * \note
     * If the user's environment defines a
     * USD_CPP_UTILITIES_SCALE_UPPER_BOUND variable, it is read as a float
     * and used. Otherwise, 0.0001 is the fallback value.
     *
     * \return Every Prim which is a PointInstancer with at least one bad scale element.
     *
     */
    _InstancerPairs get_bad_scale_values(pxr::UsdPrimRange range);
}
