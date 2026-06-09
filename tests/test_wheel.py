"""Wheel verification tests — mirrors Semaphore 'Wheel Verification' jobs."""

import confluent_kafka
from confluent_kafka import Producer


def test_version():
    v = confluent_kafka.version()
    print(f"version: {v}")
    assert v


def test_openssl():
    Producer({"ssl.cipher.suites": "DEFAULT"})
    print("OK: OpenSSL")


def test_gzip():
    Producer({"compression.codec": "gzip"})
    print("OK: gzip")


def test_lz4():
    Producer({"compression.codec": "lz4"})
    print("OK: lz4")


def test_snappy():
    Producer({"compression.codec": "snappy"})
    print("OK: snappy")


def test_zstd():
    Producer({"compression.codec": "zstd"})
    print("OK: zstd")
