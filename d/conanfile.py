from conans import CMake, ConanFile, tools


class DConan(ConanFile):
    name = "demod"
    python_requires = "base/0.1@user/dev"
    python_requires_extend = "base.Base"

    requires = "democ/0.1@user/dev"
