cmake_minimum_required(VERSION 3.26)

project(GFM_GFL_IBR)

add_library(GFM_GFL_IBR SHARED 
 GFM_GFL_IBR.c)
add_executable (test test.c)

include_directories(../include)

if(WIN32)
  target_compile_options(GFM_GFL_IBR PUBLIC "-D_USRDLL")
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

