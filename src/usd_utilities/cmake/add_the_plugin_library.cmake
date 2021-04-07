# Add a basic definition for this USD C++ library.
#
# This definition will be exported and given Python bindings. But not
# in this file.  This file focuses just on the basic definition of the
# plugin.
#
add_library(${PLUGIN_NAME}
    SHARED
        private/common.cpp
        scale_check.cpp
)

target_include_directories(${PLUGIN_NAME}
    PRIVATE
        ${PYTHON_INCLUDE_PATH}
        ${PXR_INCLUDE_DIRS}
)

target_link_libraries(${PLUGIN_NAME}
    ${PXR_sdf_LIBRARY}
    ${PXR_usd_LIBRARY}
    ${PXR_usdGeom_LIBRARY}
    ${PXR_vt_LIBRARY}
    ${USD_BOOST_PYTHON}
)
