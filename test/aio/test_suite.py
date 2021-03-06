#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from lsh_test import TestAsyncMinHashLSH, TestWeightedMinHashLSH, DO_TEST_REDIS, DO_TEST_MONGO


def test_suite_minhashlsh_aioredis():
    suite = unittest.TestSuite()
    suite.addTest(TestAsyncMinHashLSH('test_init_redis'))
    suite.addTest(TestAsyncMinHashLSH('test__H_redis'))
    suite.addTest(TestAsyncMinHashLSH('test_insert_redis'))
    suite.addTest(TestAsyncMinHashLSH('test_query_redis'))
    suite.addTest(TestAsyncMinHashLSH('test_remove_redis'))
    suite.addTest(TestAsyncMinHashLSH('test_pickle_redis'))
    suite.addTest(TestAsyncMinHashLSH('test_insertion_session_redis'))
    suite.addTest(TestAsyncMinHashLSH('test_get_counts_redis'))
    return suite


def test_suite_minhashlsh_aiomongo():
    suite = unittest.TestSuite()
    suite.addTest(TestAsyncMinHashLSH('test_init_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test__H_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test_insert_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test_query_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test_remove_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test_pickle_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test_insertion_session_mongo'))
    suite.addTest(TestAsyncMinHashLSH('test_get_counts_mongo'))
    return suite


def test_suite_weightedminhashlsh_aioredis():
    suite = unittest.TestSuite()
    suite.addTest(TestWeightedMinHashLSH('test_init_redis'))
    suite.addTest(TestWeightedMinHashLSH('test__H_redis'))
    suite.addTest(TestWeightedMinHashLSH('test_insert_redis'))
    suite.addTest(TestWeightedMinHashLSH('test_query_redis'))
    suite.addTest(TestWeightedMinHashLSH('test_remove_redis'))
    suite.addTest(TestWeightedMinHashLSH('test_pickle_redis'))
    return suite


def test_suite_weightedminhashlsh_aiomongo():
    suite = unittest.TestSuite()
    suite.addTest(TestWeightedMinHashLSH('test_init_mongo'))
    suite.addTest(TestWeightedMinHashLSH('test__H_mongo'))
    suite.addTest(TestWeightedMinHashLSH('test_insert_mongo'))
    suite.addTest(TestWeightedMinHashLSH('test_query_mongo'))
    suite.addTest(TestWeightedMinHashLSH('test_remove_mongo'))
    suite.addTest(TestWeightedMinHashLSH('test_pickle_mongo'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    if DO_TEST_REDIS:
        runner.run(test_suite_minhashlsh_aioredis())
        runner.run(test_suite_weightedminhashlsh_aioredis())
    if DO_TEST_MONGO:
        runner.run(test_suite_minhashlsh_aiomongo())
        runner.run(test_suite_weightedminhashlsh_aiomongo())
