cmake_minimum_required(VERSION 3.26)

SET(CMAKE_INSTALL_PREFIX ../..)
project(HWPV)

add_library(HWPV SHARED hwpv.c)
add_executable (TEST_HWPV test_hwpv.c)

include_directories(../include)

if(WIN32)
  target_compile_options(HWPV PUBLIC "-D_USRDLL")
  target_link_libraries(TEST_HWPV PRIVATE ../../lib/DLLWrapper)
  target_link_libraries(HWPV PRIVATE ../../lib/jansson)
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

install(TARGETS HWPV RUNTIME DESTINATION bin)
install(TARGETS TEST_HWPV RUNTIME DESTINATION bin)

