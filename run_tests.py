#!/usr/bin/env python3

import argparse
import json
import logging
import os
import random
import shutil
import sys
import tempfile
import unittest
import run_mtblisa

# create a logger instance
logger = logging.getLogger("test_logger")

# a valid study ID from the Metabolights database
_STUDY = "MTBLS9"


class MtblsIsaTests(unittest.TestCase):
    def _assert_not_empty_folder(self, result):
        self.assertIsNotNone(result, "Empty output path")
        self.assertTrue(os.path.isdir(result) > 0, "Output path is not a folder")
        self.assertTrue(len(os.listdir(result)) > 0, "Output path is empty")
        logger.debug("Output path: %s", result)

    def _assert_not_empty_json_data(self, result):
        # check result is not empty
        self.assertTrue(os.path.isfile(result))
        with open(result) as fd:
            loaded_json = json.load(fd)
            self.assertGreater(len(loaded_json), 0)

    def _clean_output(self, path):
        # remove the output path
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        elif os.path.exists(path):
            os.remove(path)
        if os.path.exists(path):
            logger.error("Error when cleaning the output path %s", path)

    def _make_tmp_name(self):
        return os.path.join(
            tempfile.gettempdir(),
            "run_mtblisa_test.{:05d}".format(random.randrange(10000)))

    def test_get_study_tab(self):
        rand_name = self._make_tmp_name()
        args = ['mtbls-get-study', _STUDY, '--isa-format', "isa-tab", rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_folder(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_get_study_json(self):
        rand_name = self._make_tmp_name()
        args = ['mtbls-get-study', _STUDY, '--isa-format', "isa-json", rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_folder(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_get_factors(self):
        rand_name = self._make_tmp_name()
        args = ['mtbls-get-factors', _STUDY, rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_get_factor_values_queries(self):
        rand_name = self._make_tmp_name()
        args = ['mtbls-get-factor-values', _STUDY, "Compound", rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_get_summary(self):
        rand_name = self._make_tmp_name()
        args = ['mtbls-get-factors-summary', _STUDY, rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_get_data_files_with_queries(self):
        rand_name = self._make_tmp_name()
        args = ['mtbls-get-data-list', _STUDY, rand_name, '--json-query',
                '{"Compound":"control 1"}']
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_get_study_archive(self):
        rand_name = self._make_tmp_name()
        fmt = 'zip'
        args = ['mtbls-get-study-archive', '--format', fmt, _STUDY, rand_name]
        archive_name = "{}.{}".format(rand_name, fmt)
        try:
            run_mtblisa.main(args)
            self.assertTrue(os.path.exists(archive_name))
        finally:
            self._clean_output(archive_name)

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', choices=[
        'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'],
                        default='INFO', help="Set the desired logging level")
    parser.add_argument('--fail-fast', default=False, action='store_true')

    return parser.parse_args(args)


class IsaSlicerTests(unittest.TestCase):

    _STUDY_PATH = "/files/galaxy/tools/slicer/test-data/MTBLS1/"

    def _assert_not_empty_folder(self, result):
        self.assertIsNotNone(result, "Empty output path")
        self.assertTrue(os.path.isdir(result) > 0, "Output path is not a folder")
        self.assertTrue(len(os.listdir(result)) > 0, "Output path is empty")
        logger.debug("Output path: %s", result)

    def _assert_not_empty_json_data(self, result):
        # check result is not empty
        self.assertTrue(os.path.isfile(result))
        with open(result) as fd:
            loaded_json = json.load(fd)
            self.assertGreater(len(loaded_json), 0)

    def _clean_output(self, path):
        # remove the output path
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        elif os.path.exists(path):
            os.remove(path)
        if os.path.exists(path):
            logger.error("Error when cleaning the output path %s", path)

    def _make_tmp_name(self):
        return os.path.join(
            tempfile.gettempdir(),
            "run_mtblisa_test.{:05d}".format(random.randrange(10000)))

    def test_isatab_get_factors(self):
        rand_name = self._make_tmp_name()
        args = ['isa-tab-get-factors', self._STUDY_PATH, rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_isatab_get_factor_values_queries(self):
        rand_name = self._make_tmp_name()
        args = ['isa-tab-get-factor-values', self._STUDY_PATH, "Gender", rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_isatab_get_summary(self):
        rand_name = self._make_tmp_name()
        args = ['isa-tab-get-factors-summary', self._STUDY_PATH, rand_name]
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    def test_isatab_get_data_files_list_with_queries(self):
        rand_name = self._make_tmp_name()
        args = ['isa-tab-get-data-list', self._STUDY_PATH, rand_name, '--json-query',
                '{"Gender":"Male"}']
        try:
            run_mtblisa.main(args)
            self._assert_not_empty_json_data(rand_name)
        finally:
            self._clean_output(rand_name)

    # Commented out until figure out how to use input data collection
    # def test_isatab_get_data_files_collection_with_queries(self):
    #     rand_name = self._make_tmp_name()
    #     args = ['isa-tab-get-data-collection', self._STUDY_PATH, rand_name, '--json-query',
    #             '{"Gender":"Male"}']
    #     try:
    #         run_mtblisa.main(args)
    #         self._assert_not_empty_folder(rand_name)
    #     finally:
    #         self._clean_output(rand_name)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    opts = parse_args(args)

    logging_level = getattr(logging, opts.log_level, logging.INFO)
    logging.basicConfig(level=logging_level)
    logger.setLevel(logging_level)

    # configure and run tests
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MtblsIsaTests)
    result1 = unittest.TextTestRunner(
        verbosity=2, failfast=opts.fail_fast).run(suite1)

    # configure and run tests
    suite2 = unittest.TestLoader().loadTestsFromTestCase(IsaSlicerTests)
    result2 = unittest.TextTestRunner(
        verbosity=2, failfast=opts.fail_fast).run(suite2)

    return result1.wasSuccessful() == result2.wasSuccessful()


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
