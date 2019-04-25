# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class SPIRVConan(ConanFile):
    name = "spirv-headers"
    version = "1.3.7"
    description = "Khronos SPIRV-Headers"
    topics = ("spirv")
    url = "https://github.com/bincrafters/conan-spirv-headers"
    homepage = "https://github.com/KhronosGroup/SPIRV-Headers"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/KhronosGroup/SPIRV-Headers"
        checksum = "60c48b0bd0c364a69edd36ddf576a6b440babc99d9822961accbbcbc5794dd7e"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version), sha256=checksum)
        extracted_dir = "SPIRV-Headers-" + self.version

        # Rename to "source_subfolder" is a convention to simplify later steps
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