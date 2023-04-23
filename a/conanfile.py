from conans import ConanFile


class AConan(ConanFile):
    name = "demoa"
    python_requires = "base/0.1@user/dev"
    python_requires_extend = "base.Base"

    # requires = "base/0.1@user/dev"

    def package_info(self):
        self.cpp_info.libs = ["demoa"]
