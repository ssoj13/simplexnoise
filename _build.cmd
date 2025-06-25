@echo off
cls
rem rd /s /q build
mkdir build
cd build
cmake --log-level ERROR ../ -G "Visual Studio 17 2022" "-DVCPKG_TARGET_TRIPLET=x64-windows" && cmake --build . --target ALL_BUILD --config Release
pause
cmake -P cmake_install.cmake