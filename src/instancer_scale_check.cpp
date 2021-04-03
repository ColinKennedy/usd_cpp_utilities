#include <iostream>
#include <utility>
#include <vector>

#include <pxr/base/vt/types.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/pointInstancer.h>

#include "instancer_scale_check.h"


using _Indices = std::vector<int>;


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
    _InstancerIndices get_bad_scale_values(pxr::UsdPrimRange range)
    {
        _InstancerIndices output;

        auto instancers = _get_instancers(range);

        for (auto const &instancer : instancers)
        {
            _Indices indices;

            auto attribute = instancer.GetPositionsAttr();
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
                // output.push_back(std::make_pair(instancer.GetPrim(), indices));
                auto pair = std::make_pair(1, 13);

                return pair;
                // output.emplace_back(1, 12);
            }
        }

        auto pair = std::make_pair(1, 14);

        return pair;
        // return output;
    }
}
