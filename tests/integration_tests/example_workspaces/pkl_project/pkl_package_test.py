# Copyright © 2024 Apple Inc. and the Pkl project authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import unittest
import zipfile
import tempfile

from pathlib import Path
from bazel_tools.tools.python.runfiles import runfiles


class MyTestCase(unittest.TestCase):
    def test_pklproject_has_been_evaluated_successfully(self):
        # The test is executed only if 'PklProject' is valid and has been evaluated successfully.
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
