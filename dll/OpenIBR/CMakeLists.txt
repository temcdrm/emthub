cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ..)
project(OPENIBR)

add_library(OPENIBR SHARED OpenIBR.c)
add_executable (TEST_OPENIBR test_OpenIBR.c)

include_directories(../include)

cmake_print_variables (CMAKE_INSTALL_PREFIX PROJECT_SOURCE_DIR CMAKE_GENERATOR_PLATFORM)

if(WIN32)
  target_compile_options(OPENIBR PUBLIC "-D_USRDLL")
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

if("${CMAKE_GENERATOR_PLATFORM}" STREQUAL "Win32")
  install(TARGETS OPENIBR RUNTIME DESTINATION bin32)
  install(TARGETS TEST_OPENIBR RUNTIME DESTINATION bin32)
  target_link_libraries(TEST_OPENIBR PRIVATE ../../lib32/DLLWrapper)
else()
  install(TARGETS OPENIBR RUNTIME DESTINATION bin)
  install(TARGETS TEST_OPENIBR RUNTIME DESTINATION bin)
  target_link_libraries(TEST_OPENIBR PRIVATE ../../lib/DLLWrapper)
endif()
