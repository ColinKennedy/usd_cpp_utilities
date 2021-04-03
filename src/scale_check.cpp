#include <utility>
#include <vector>

#include <pxr/base/vt/types.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/pointInstancer.h>

#include "scale_check.h"
#include "common.h"


static auto _UPPER_BOUND = _get_upper_bound();

inline bool _is_too_low(float value)
{
    return std::abs(value) < _UPPER_BOUND;
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
