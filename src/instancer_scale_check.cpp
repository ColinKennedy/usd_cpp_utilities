#include <iostream>

#include <pxr/usd/usd/stage.h>


namespace usd_utilities
{
    int get_bad_scale_values()
    {
        auto stage = pxr::UsdStage::Open("/tmp/place.usdc");
        std::cout << stage->GetRootLayer()->GetIdentifier() << "\n";

        return 8;
    }
}
