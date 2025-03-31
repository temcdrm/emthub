cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ..)
project(HWPV)

add_library(HWPV SHARED hwpv.c)
add_executable (TEST_HWPV test_hwpv.c)

include_directories(../include)

cmake_print_variables (CMAKE_INSTALL_PREFIX PROJECT_SOURCE_DIR CMAKE_GENERATOR_PLATFORM)

if(WIN32)
  target_compile_options(HWPV PUBLIC "-D_USRDLL")
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

install(TARGETS HWPV RUNTIME DESTINATION bin)
install(TARGETS TEST_HWPV RUNTIME DESTINATION bin)
if("${CMAKE_GENERATOR_PLATFORM}" STREQUAL "Win32")
  install(TARGETS HWPV RUNTIME DESTINATION bin32)
  install(TARGETS TEST_HWPV RUNTIME DESTINATION bin32)
  target_link_libraries(TEST_HWPV PRIVATE ../../lib32/DLLWrapper)
  target_link_libraries(HWPV PRIVATE ../../lib32/jansson)
else()
  install(TARGETS HWPV RUNTIME DESTINATION bin)
  install(TARGETS TEST_HWPV RUNTIME DESTINATION bin)
  target_link_libraries(TEST_HWPV PRIVATE ../../lib/DLLWrapper)
  target_link_libraries(HWPV PRIVATE ../../lib/jansson)
endif()
