# Export a namespace for this library so other C++ projects can use it
#
# Reference: https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/
#
set(PLUGIN_TARGETS_NAME UsdUtilitiesTargets)
set(INSTALL_CONFIGURATION_DIRECTORY lib/cmake/UsdUtilities)

# 1. Add individual export targets
install(
    TARGETS scale_check
    EXPORT ${PLUGIN_TARGETS_NAME}
    LIBRARY DESTINATION lib
    INCLUDES DESTINATION include
)

install(
    TARGETS itermaker
    EXPORT ${PLUGIN_TARGETS_NAME}
    LIBRARY DESTINATION lib
    INCLUDES DESTINATION include
)

# 2. Now export everything, under the usd_utilities:: namespace
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

configure_package_config_file(${CMAKE_CURRENT_LIST_DIR}/UsdUtilitiesConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/UsdUtilitiesConfig.cmake
    INSTALL_DESTINATION ${INSTALL_CONFIGURATION_DIRECTORY}
)

# Copy the generated UsdUtilitiesConfig.cmake to the installation directory.
install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/UsdUtilitiesConfig.cmake
    DESTINATION ${INSTALL_CONFIGURATION_DIRECTORY}
)
