cmake_minimum_required(VERSION 3.16)
project(simplexnoise VERSION 1.0.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Use GNUInstallDirs for standard installation paths
include(GNUInstallDirs)

# Collect source files
file(GLOB SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)
file(GLOB HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.h)

# Create static library
add_library(simplexnoise STATIC ${SOURCES} ${HEADERS})

# Set include directories
target_include_directories(simplexnoise PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

# Create alias for modern CMake usage
add_library(simplexnoise::simplexnoise ALIAS simplexnoise)

# Installation
install(TARGETS simplexnoise
    EXPORT simplexnoiseTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# Install headers
install(FILES ${HEADERS}
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/simplexnoise
)

# Install export targets
install(EXPORT simplexnoiseTargets
    FILE simplexnoiseTargets.cmake
    NAMESPACE simplexnoise::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/simplexnoise
)

# Generate and install config files
include(CMakePackageConfigHelpers)

# Create the config file
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/simplexnoiseConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/simplexnoiseConfig.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/simplexnoise
)

# Create the version file
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/simplexnoiseConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

# Install config files
install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/simplexnoiseConfig.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/simplexnoiseConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/simplexnoise
)