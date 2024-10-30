cmake_minimum_required(VERSION 3.26)

project(SCRX9)

add_library(SCRX9 SHARED SCRX9.c)
add_executable (test test.c)
add_executable (test_wrapper test_wrapper.c IEEE_Cigre_DLLWrapper.c)

include_directories(../include)

if(WIN32)
  target_compile_options(SCRX9 PUBLIC "-D_USRDLL")
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

