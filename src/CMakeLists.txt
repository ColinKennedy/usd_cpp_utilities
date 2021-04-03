# TODO : Remove this foo.cpp, later
add_library(${PLUGIN_NAME}
    SHARED
        foo.cpp
)

install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
