include(cmake/add_the_plugin_library.cmake)
include(cmake/export_the_plugin.cmake)

# Copy the header files so external packages can include + use them
install(
    DIRECTORY
        include
    DESTINATION
        include
)

# Copy the generated libraries (the .so files)
install(
    TARGETS ${PLUGIN_NAME}
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
