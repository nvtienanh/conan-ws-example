cmake_minimum_required(VERSION 3.16 FATAL_ERROR)
project(DemoB)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_C_STANDARD 99)

if(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo_multi.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo_multi.cmake)
else()
    include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
endif()

conan_basic_setup(TARGETS)

add_subdirectory(src)
enable_testing()
add_subdirectory(test)
