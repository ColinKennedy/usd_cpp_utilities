# Add the Python bindings
set(PLUGIN_PYTHON_NAME scale_check)

add_library(${PLUGIN_PYTHON_NAME}
    SHARED
        wrap_scale_check.cpp
)

# TODO : Can I just point ${PLUGIN_NAME} here, maybe?
target_include_directories(${PLUGIN_PYTHON_NAME}
    PRIVATE
        ${PYTHON_INCLUDE_PATH}
        ${PXR_INCLUDE_DIRS}
        ../usd_utilities/include
        ../usd_utilities/private
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
