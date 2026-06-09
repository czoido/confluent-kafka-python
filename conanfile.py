from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class ConfluentKafkaPythonConan(ConanFile):
    name = "confluent-kafka"
    version = "2.14.2"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("librdkafka/2.14.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
