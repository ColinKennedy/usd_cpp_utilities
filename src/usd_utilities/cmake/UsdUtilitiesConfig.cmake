get_filename_component(CUSTOM_SCHEMAS_DIRECTORY "${CMAKE_CURRENT_LIST_FILE}" PATH)

find_package(PythonLibs REQUIRED)

if(NOT TARGET usd_utilities::usd_utilities)
    include("${CUSTOM_SCHEMAS_DIRECTORY}/UsdUtilitiesTargets.cmake")
endif()
