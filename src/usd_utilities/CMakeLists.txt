# Add all files and link them to USD / boost
set(PLUGIN_NAME usd_cpp_utilities_plugin)

add_library(${PLUGIN_NAME}
    SHARED
        common.cpp
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

# Create a Config.cmake file so that other C++ projects can use
# `find_package` to get the namespace that was exported in step #5
#
# Reference: https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right
#
include(CMakePackageConfigHelpers)

configure_package_config_file(${CMAKE_CURRENT_LIST_DIR}/cmake/UsdUtilitiesConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/UsdUtilitiesConfig.cmake
    INSTALL_DESTINATION ${INSTALL_CONFIGURATION_DIRECTORY}
)

install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/UsdUtilitiesConfig.cmake
    DESTINATION ${INSTALL_CONFIGURATION_DIRECTORY}
)

# Copy the header files so external packages can include + use them
install(
    FILES
        scale_check.h
    DESTINATION
        include
)

# Copy the generated libraries (the .so files)
install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
