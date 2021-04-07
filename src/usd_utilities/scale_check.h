#pragma once

/** \file scale_check.h
 *
 * The main module for finding bad scale values in a USD scene.  In this
 * case, "bad" means "A scale value which is on-or-approaching zero".
 * By default, this value is 0.0001. But you can set it to a lower
 * or higher value, using the "USD_CPP_UTILITIES_SCALE_UPPER_BOUND"
 * environment variable.
 *
 */

#include <utility>
#include <vector>

#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>


using _Indices = std::vector<int>;
using _InstancerPair = std::pair<pxr::UsdPrim, _Indices>;
using _InstancerPairs = std::vector<_InstancerPair>;


/**
 * \namespace usd_utilities
 * \brief All public objects in this Rez package which external packages may use.
 */
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
    _InstancerPairs get_bad_scale_values(pxr::UsdPrimRange const &range);
}
