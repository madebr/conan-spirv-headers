# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class SPIRVConan(ConanFile):
    name = "spirv-headers"
    version = "1.4.1"
    description = "Khronos SPIRV-Headers"
    topics = ("conan", "spirv")
    url = "https://github.com/bincrafters/conan-spirv-headers"
    homepage = "https://github.com/KhronosGroup/SPIRV-Headers"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/KhronosGroup/SPIRV-Headers"
        checksum = "a244f0629f75eb450e090cd773d30e22367cb231e964c7492588eb9000201fd1"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version), sha256=checksum)
        extracted_dir = "SPIRV-Headers-" + self.version

        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()
