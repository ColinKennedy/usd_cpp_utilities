# TODO : Remove this foo.cpp, later
add_library(${PLUGIN_NAME}
    SHARED
        instancer_scale_check.cpp
)

target_include_directories(${PLUGIN_NAME}
PUBLIC
    ${PYTHON_INCLUDE_PATH}
    ${PXR_INCLUDE_DIRS}
)

target_link_libraries(${PLUGIN_NAME}
    ${PXR_sdf_LIBRARY}
)

install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
