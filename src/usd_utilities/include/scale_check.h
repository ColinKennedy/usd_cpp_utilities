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

#include <pxr/usd/usd/primRange.h>

#include "common.h"


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
     * \param range: The Prims to check for PointInstancers and invalid scale indices.
     *
     * \return Every Prim which is a PointInstancer with at least one bad scale element.
     *
     */
    InstancerPairs get_bad_scale_values(pxr::UsdPrimRange const &range);
}
