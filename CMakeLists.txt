cmake_minimum_required(VERSION 2.8.11)
project(usd_cpp_utilities)

find_package(PythonLibs REQUIRED)
find_package(pxr REQUIRED)

find_library(USD_BOOST_PYTHON
    boost_python NAMES boost_python36
    HINTS ${PXR_CMAKE_DIR}/lib
)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(PLUGIN_NAME usd_cpp_utilities_plugin)

add_subdirectory(src)
