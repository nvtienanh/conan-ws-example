from conans import CMake, ConanFile, tools


class CConan(ConanFile):
    name = "democ"
    python_requires = "base/0.1@user/dev"
    python_requires_extend = "base.Base"

    requires = "demob/0.1@user/dev"

    def package_info(self):
        self.cpp_info.libs = ["democ"]
