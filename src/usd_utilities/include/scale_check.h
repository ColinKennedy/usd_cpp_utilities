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

#include <pxr/usd/usd/attribute.h>

#include "common.h"

/**
 * \namespace usd_utilities
 * \brief All public objects in this Rez package which external packages may
 * use.
 */
namespace usd_utilities {
/** \brief Find index in an attribute with small scale elements.
 *
 * \note
 * If the user's environment defines a
 * USD_CPP_UTILITIES_SCALE_UPPER_BOUND variable, it is read as a float
 * and used. Otherwise, 0.0001 is the fallback value.
 *
 * \param attribute: The USD object to check for zeroed indices.
 *
 * \return Every index in the Attribute with at least one bad scale element.
 *
 */
Indices get_bad_scale_values(pxr::UsdAttribute const &attribute);
} // namespace usd_utilities
