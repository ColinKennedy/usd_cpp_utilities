set(PYTHON_PACKAGE_NAME usd_utilities)
set(PYTHON_PACKAGE_RELATIVE_PATH lib/python/${PYTHON_PACKAGE_NAME})
set(INSTALL_PYTHON_PACKAGE ${PYTHON_PACKAGE_RELATIVE_PATH})

function(make_python_binding target_name)
    add_library(${target_name}_python
        SHARED
            wrap_${target_name}.cpp
    )

    target_include_directories(${target_name}_python
        PRIVATE
            ${PYTHON_INCLUDE_PATH}
            ${PXR_INCLUDE_DIRS}
            ../usd_utilities/include
            ../usd_utilities/private
    )

    target_link_libraries(${target_name}_python
        ${target_name}
    )

    # On OSX "dylib" does not work to import python module
    set_target_properties(${target_name}_python PROPERTIES SUFFIX ".so")

    set_target_properties(${target_name}_python
        PROPERTIES
            PREFIX ""
            OUTPUT_NAME ${target_name}
    )

    install(
        TARGETS ${target_name}_python
        DESTINATION ${INSTALL_PYTHON_PACKAGE}
    )
endfunction()

# 1. Make each individual Python module
make_python_binding(scale_check)
make_python_binding(itermaker)

# 2. Copy all of the modules under a single Python namespace
install(
    FILES __packageinit__.py
    DESTINATION ${INSTALL_PYTHON_PACKAGE}
    RENAME __init__.py
)
