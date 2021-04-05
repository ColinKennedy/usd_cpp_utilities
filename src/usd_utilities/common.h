#pragma once

/** \file common.h
 *
 * Any private or public functions which makes writing C++ code easier.
 *
 */

#include <vector>

#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usdGeom/pointInstancer.h>


/** \brief Find all PointInstancers in a range of possible Prims.
 *
 * \param range The Prims to consider from 1-or-more stages.
 *
 * \return All found PointInstancer Prims, if any.
 */
std::vector<pxr::UsdGeomPointInstancer> _get_instancers(pxr::UsdPrimRange range);


/** \brief Find the maximum value which "bad" scale component values may be.
 *
 * Any PointInstancer whose scale attribute contains a component whose
 * value is on-or-less than this will be considered "too small" and thus,
 * "bad".
 *
 * \note
 * If the user's environment defines a
 * USD_CPP_UTILITIES_SCALE_UPPER_BOUND variable, it is read as a float
 * and used. Otherwise, 0.0001 is the fallback value.
 *
 * \return The found value.
 */
float _get_upper_bound();
