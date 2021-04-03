#include <iostream>
#include <utility>
#include <vector>

#include <pxr/base/vt/types.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/pointInstancer.h>

#include "instancer_scale_check.h"


inline bool _is_too_low(float value)
{
    return std::abs(value) < 0.0001;
}

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

namespace usd_utilities
{
    _InstancerPairs get_bad_scale_values(pxr::UsdPrimRange range)
    {
        _InstancerPairs output;

        for (auto const &instancer : _get_instancers(range))
        {
            _Indices indices;

            auto attribute = instancer.GetScalesAttr();
            pxr::VtVec3fArray values;
            attribute.Get(&values);

            for (int index = 0; index < values.size(); ++index)
            {
                auto value = values[index];

                if (
                    _is_too_low(value[0])
                    || _is_too_low(value[1])
                    || _is_too_low(value[2])
                )
                {
                    indices.push_back(index);
                }
            }

            if (!indices.empty())
            {
                output.emplace_back(instancer.GetPrim(), indices);
            }
        }

        return output;
    }
}
