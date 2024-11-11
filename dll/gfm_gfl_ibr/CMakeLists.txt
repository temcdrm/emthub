cmake_minimum_required(VERSION 3.26)

SET(CMAKE_INSTALL_PREFIX ../..)
project(GFM_GFL_IBR)

add_library(GFM_GFL_IBR SHARED GFM_GFL_IBR.c)
add_executable (TEST_IBR test_ibr.c)

include_directories(../include)

if(WIN32)
  target_compile_options(GFM_GFL_IBR PUBLIC "-D_USRDLL")
  target_link_libraries(TEST_IBR PRIVATE ../../lib/DLLWrapper)
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

install(TARGETS GFM_GFL_IBR RUNTIME DESTINATION bin)
install(TARGETS TEST_IBR RUNTIME DESTINATION bin)

