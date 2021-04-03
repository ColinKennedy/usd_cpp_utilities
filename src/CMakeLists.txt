# Add all files and link them to USD / boost
add_library(${PLUGIN_NAME}
    SHARED
        instancer_scale_check.cpp
        wrap_instancer_scale_check.cpp
)

target_include_directories(${PLUGIN_NAME}
PUBLIC
    ${PYTHON_INCLUDE_PATH}
    ${PXR_INCLUDE_DIRS}
)

target_link_libraries(${PLUGIN_NAME}
    ${PXR_sdf_LIBRARY}
    ${USD_BOOST_PYTHON}
)

set(PLUGIN_TARGETS_NAME UsdUtilitiesTargets)
set(INSTALL_CONFIGURATION_DIRECTORY lib/cmake/UsdUtilities)

# Export a namespace for this library so other C++ projects can use it
#
# Reference: https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/
#
install(
    TARGETS ${PLUGIN_NAME}
    EXPORT ${PLUGIN_TARGETS_NAME}
    LIBRARY DESTINATION lib
    INCLUDES DESTINATION include
)

install(
    EXPORT ${PLUGIN_TARGETS_NAME}
    FILE ${PLUGIN_TARGETS_NAME}.cmake
    NAMESPACE usd_utilities::
    DESTINATION ${INSTALL_CONFIGURATION_DIRECTORY}
)

# Copy the header files so external packages can include + use them
install(
    FILES
        instancer_scale_check.h
    DESTINATION
        include
)

# Copy the generated libraries (the .so files)
install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
