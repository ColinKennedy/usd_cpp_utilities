cmake_minimum_required(VERSION 2.8.11)
project(usd_cpp_utilities)

find_package(pxr)

set(PLUGIN_NAME usd_cpp_utilities_plugin)

add_subdirectory(src)
