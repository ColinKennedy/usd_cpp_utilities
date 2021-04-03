#include <pxr/usd/usd/stage.h>


void get_bad_scale_values()
{
    auto stage = pxr::UsdStage::Open("/tmp/place.usdc");
}
