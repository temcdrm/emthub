cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ..)
project(DLLWrapper)

add_library(DLLWrapper STATIC IEEE_Cigre_DLLWrapper.c)

include_directories(../include)

cmake_print_variables (CMAKE_INSTALL_PREFIX PROJECT_SOURCE_DIR CMAKE_GENERATOR_PLATFORM)

if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

if("${CMAKE_GENERATOR_PLATFORM}" STREQUAL "Win32")
  message("for win32")
  install(TARGETS DLLWrapper ARCHIVE DESTINATION lib32)
else()
  message("NOT for win32")
  install(TARGETS DLLWrapper ARCHIVE DESTINATION lib)
endif()
