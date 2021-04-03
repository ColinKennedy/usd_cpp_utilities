# TODO : Remove this foo.cpp, later
add_library(${PLUGIN_NAME}
    SHARED
        foo.cpp
)

target_link_libraries(${PLUGIN_NAME}
    ${PXR_sdf_LIBRARY}
)

install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
