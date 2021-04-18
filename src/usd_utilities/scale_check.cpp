#include <cmath>
#include <utility>
#include <vector>

#include <pxr/base/vt/types.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/pointInstancer.h>

#include "scale_check.h"
#include "private/common.h"


static auto UPPER_BOUND = get_upper_bound();

inline static bool is_too_low(float value)
{
    return std::abs(value) < UPPER_BOUND;
}


namespace usd_utilities
{
    InstancerPairs get_bad_scale_values(pxr::UsdPrimRange const &range)
    {
        InstancerPairs output;

        for (auto const &instancer : get_instancers(range))
        {
            Indices indices;

            auto attribute = instancer.GetScalesAttr();
            pxr::VtVec3fArray values;
            attribute.Get(&values);

            for (int index = 0; index < values.size(); ++index)
            {
                auto value = values[index];

                if (
                    is_too_low(value[0])
                    || is_too_low(value[1])
                    || is_too_low(value[2])
                )
                {
                    indices.push_back(index);
                }
            }

            if (!indices.empty())
            {
                output.emplace_back(attribute, indices);
            }
        }

        return output;
    }
}
