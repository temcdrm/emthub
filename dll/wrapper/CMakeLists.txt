cmake_minimum_required(VERSION 3.26)

SET(CMAKE_INSTALL_PREFIX ../..)
project(DLLWrapper)

add_library(DLLWrapper STATIC IEEE_Cigre_DLLWrapper.c)

include_directories(../include)

#if(WIN32)
#  target_compile_options(DLLWrapper PUBLIC "-D_USRDLL")
#endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

#install(TARGETS DLLWrapper DESTINATION "${CMAKE_SOURCE_DIR}/Lib")
install(TARGETS DLLWrapper ARCHIVE DESTINATION lib)
