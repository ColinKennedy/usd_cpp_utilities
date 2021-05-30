include(cmake/add_scale_check.cmake)
include(cmake/export_scale_check.cmake)

# Copy the header files so external packages can include + use them
install(
    DIRECTORY
        include
    DESTINATION
        include
)

# Copy the generated libraries (the .so files)
install(
    TARGETS scale_check
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
