```bash
#gcc/g++ -v 11

conan remove "demo*" -f
conan export . base/0.1@user/dev

mkdir build
conan workspace install ../.config/workspace/ws-linux.yml \
                --install-folder . \
                --profile ../.config/conan_config/profiles/ubuntu-gcc-release
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build .
```