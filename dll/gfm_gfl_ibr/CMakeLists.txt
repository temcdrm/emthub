cmake_minimum_required(VERSION 3.26)

project(GFM_GFL_IBR)

add_library(GFM_GFL_IBR SHARED 
 GFM_GFL_IBR.c)

include_directories(../include)

if(WIN32)
  target_compile_options(GFM_GFL_IBR PUBLIC "-D_USRDLL")
#  target_sources(GFM_GFL_IBR PRIVATE GFM_GFL_IBR.def)
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

# target_link_libraries(GFM_GFL_IBR)
