add_library(itermaker
    SHARED
        itermaker.cpp
)

target_include_directories(itermaker
    PRIVATE
        ${PYTHON_INCLUDE_PATH}
        ${PXR_INCLUDE_DIRS}
)

target_link_libraries(itermaker
    ${PXR_sdf_LIBRARY}
    ${PXR_tf_LIBRARY}
    ${USD_BOOST_PYTHON}
)

# Copy the generated libraries (the .so files)
install(
    TARGETS itermaker
    DESTINATION ${REZ_BUILD_INSTALL_PATH}
)
