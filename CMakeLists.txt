cmake_minimum_required(VERSION 3.15)
project(confluent_kafka_cimpl LANGUAGES C)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(RdKafka CONFIG REQUIRED)

Python3_add_library(cimpl MODULE WITH_SOABI
    src/confluent_kafka/src/confluent_kafka.c
    src/confluent_kafka/src/Producer.c
    src/confluent_kafka/src/Consumer.c
    src/confluent_kafka/src/Metadata.c
    src/confluent_kafka/src/AdminTypes.c
    src/confluent_kafka/src/Admin.c
)

target_link_libraries(cimpl PRIVATE RdKafka::rdkafka)

install(TARGETS cimpl DESTINATION confluent_kafka)
