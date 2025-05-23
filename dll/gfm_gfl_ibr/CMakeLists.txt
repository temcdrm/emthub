cmake_minimum_required(VERSION 3.26)

include(CMakePrintHelpers)

SET(CMAKE_INSTALL_PREFIX ..)
project(GFM_GFL_IBR)

add_library(GFM_GFL_IBR SHARED GFM_GFL_IBR.c)
add_executable (TEST_IBR test_ibr.c)

include_directories(../include)

cmake_print_variables (CMAKE_INSTALL_PREFIX PROJECT_SOURCE_DIR CMAKE_GENERATOR_PLATFORM)

if(WIN32)
  target_compile_options(GFM_GFL_IBR PUBLIC "-D_USRDLL")
endif()
if(UNIX)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()
if(APPLE)
  set(CMAKE_C_FLAGS "-O3 -fPIC")
endif()

if("${CMAKE_GENERATOR_PLATFORM}" STREQUAL "Win32")
  install(TARGETS GFM_GFL_IBR RUNTIME DESTINATION bin32)
  install(TARGETS TEST_IBR RUNTIME DESTINATION bin32)
  target_link_libraries(TEST_IBR PRIVATE ../../lib32/DLLWrapper)
else()
  install(TARGETS GFM_GFL_IBR RUNTIME DESTINATION bin)
  install(TARGETS TEST_IBR RUNTIME DESTINATION bin)
  target_link_libraries(TEST_IBR PRIVATE ../../lib/DLLWrapper)
endif()
