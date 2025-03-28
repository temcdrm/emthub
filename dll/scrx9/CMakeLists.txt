cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ../..)
project(SCRX9)

add_library(SCRX9 SHARED SCRX9.c)
add_executable (test test.c)
add_executable (TEST_SCRX9 test_scrx9.c)

include_directories(../include)

if(WIN32)
  target_compile_options(SCRX9 PUBLIC "-D_USRDLL")
  target_link_libraries(TEST_SCRX9 PRIVATE ../../lib/DLLWrapper)
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

install(TARGETS SCRX9 RUNTIME DESTINATION bin)
install(TARGETS TEST_SCRX9 RUNTIME DESTINATION bin)


