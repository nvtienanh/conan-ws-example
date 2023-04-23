from conans import ConanFile


class BConan(ConanFile):
    name = "demob"
    python_requires = "base/0.1@user/dev"
    python_requires_extend = "base.Base"

    requires = "demoa/0.1@user/dev"

    def package_info(self):
        self.cpp_info.libs = ["demob"]
