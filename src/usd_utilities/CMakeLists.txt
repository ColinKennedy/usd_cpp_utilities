include(cmake/add_scale_check.cmake)
include(cmake/add_itermaker.cmake)
include(cmake/export_all.cmake)

# Copy the header files so external packages can include + use them
install(
    DIRECTORY
        include
    DESTINATION
        include
)
