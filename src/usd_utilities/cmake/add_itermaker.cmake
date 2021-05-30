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
    ${USD_BOOST_PYTHON}
)
