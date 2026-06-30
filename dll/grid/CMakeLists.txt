cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ..)
project(GRID)

add_executable (GRID test_grid.c)

include_directories(../include)

cmake_print_variables (CMAKE_INSTALL_PREFIX PROJECT_SOURCE_DIR CMAKE_GENERATOR_PLATFORM)

if("${CMAKE_GENERATOR_PLATFORM}" STREQUAL "Win32")
  install(TARGETS GRID RUNTIME DESTINATION bin32)
else()
  install(TARGETS GRID RUNTIME DESTINATION bin)
endif()
