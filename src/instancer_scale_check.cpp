#include <iostream>
#include <vector>

#include <pxr/base/vt/types.h>
#include <pxr/usd/usdGeom/pointInstancer.h>
#include <pxr/usd/usd/primRange.h>
#include <pxr/usd/usd/stage.h>


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
    std::vector<int> get_bad_scale_values()
    {
        std::vector<int> output {8};

        // auto stage = pxr::UsdStage::Open("/tmp/place.usdc");
        // auto instancers = _get_instancers(stage->TraverseAll());

        // for (auto const &instancer : instancers)
        // {
        //     auto attribute = instancer.GetPositionsAttr();
        //     pxr::VtVec3fArray values;
        //     attribute.Get(&values);
        //
        //     for (int index = 0; index < values.size(); ++index)
        //     {
        //         auto value = values[index];
        //
        //         if (
        //             _is_too_low(value[0])
        //             || _is_too_low(value[1])
        //             || _is_too_low(value[2])
        //         )
        //         {
        //             output.push_back(index);
        //         }
        //     }
        // }

        return output;
    }
}
