# Add all files and link them to USD / boost
set(PLUGIN_NAME usd_cpp_utilities_plugin)

add_library(${PLUGIN_NAME}
    SHARED
        instancer_scale_check.cpp
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
        instancer_scale_check.h
    DESTINATION
        include
)

# Copy the generated libraries (the .so files)
install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)

# Add the Python bindings
set(PLUGIN_PYTHON_NAME instancer_scale_check)

add_library(${PLUGIN_PYTHON_NAME}
    SHARED
        wrap_instancer_scale_check.cpp
)

# TODO : Can I just point ${PLUGIN_NAME} here, maybe?
target_include_directories(${PLUGIN_PYTHON_NAME}
    PRIVATE
        ${PYTHON_INCLUDE_PATH}
        ${PXR_INCLUDE_DIRS}
)

# On OSX "dylib" does not work to import python module
# TODO: windows support
set_target_properties(${PLUGIN_PYTHON_NAME} PROPERTIES SUFFIX ".so")

set_target_properties(${PLUGIN_PYTHON_NAME}
    PROPERTIES
        PREFIX ""
)

set(PYTHON_PACKAGE_NAME usd_utilities)

# XXX : These lines "find" the Python package
target_compile_definitions(${PLUGIN_PYTHON_NAME}
    PRIVATE
        MFB_PACKAGE_NAME=${PLUGIN_NAME}
        MFB_ALT_PACKAGE_NAME=${PLUGIN_NAME}
        MFB_PACKAGE_MODULE=${PYTHON_PACKAGE_NAME}.${MODULE_NAME}
)

target_link_libraries(${PLUGIN_PYTHON_NAME}
    ${PLUGIN_NAME}
)

set(PYTHON_PACKAGE_RELATIVE_PATH lib/python/${PYTHON_PACKAGE_NAME})
set(INSTALL_PYTHON_PACKAGE ${PYTHON_PACKAGE_RELATIVE_PATH})


install(
    FILES __packageinit__.py
    DESTINATION ${INSTALL_PYTHON_PACKAGE}
    RENAME __init__.py
)

install(
    TARGETS ${PLUGIN_PYTHON_NAME}
    DESTINATION ${INSTALL_PYTHON_PACKAGE}/${MODULE_NAME}
)
