cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ..)
project(SEXS)

add_library(SEXS SHARED SEXS.c)
add_executable (TEST_SEXS test_SEXS.c)

include_directories(../include)

cmake_print_variables (CMAKE_INSTALL_PREFIX PROJECT_SOURCE_DIR CMAKE_GENERATOR_PLATFORM)

if(WIN32)
  target_compile_options(SEXS PUBLIC "-D_USRDLL")
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

if("${CMAKE_GENERATOR_PLATFORM}" STREQUAL "Win32")
  target_link_libraries(TEST_SEXS PRIVATE ../../lib32/DLLWrapper)
  install(TARGETS SEXS RUNTIME DESTINATION bin32)
  install(TARGETS TEST_SEXS RUNTIME DESTINATION bin32)
else()
  target_link_libraries(TEST_SEXS PRIVATE ../../lib/DLLWrapper)
  install(TARGETS SEXS RUNTIME DESTINATION bin)
  install(TARGETS TEST_SEXS RUNTIME DESTINATION bin)
endif()

