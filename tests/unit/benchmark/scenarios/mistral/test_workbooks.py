# Copyright 2015: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from rally.benchmark.scenarios.mistral import workbooks
from tests.unit import test

MISTRAL_WBS = "rally.benchmark.scenarios.mistral.workbooks.MistralWorkbooks"


class MistralWorkbooksTestCase(test.TestCase):

    @mock.patch(MISTRAL_WBS + "._list_workbooks")
    def test_list_workbooks(self, mock_list):
        mistral_scenario = workbooks.MistralWorkbooks()
        mistral_scenario.list_workbooks()
        mock_list.assert_called_once_with()

    @mock.patch(MISTRAL_WBS + "._create_workbook")
    def test_create_workbook(self, mock_create):
        mistral_scenario = workbooks.MistralWorkbooks()
        definition = "---\nversion: \"2.0\"\nname: wb"
        fake_wb = mock.MagicMock()
        fake_wb.name = "wb"
        mock_create.return_value = fake_wb
        mistral_scenario.create_delete_workbook(definition)

        self.assertEqual(1, mock_create.called)

    @mock.patch(MISTRAL_WBS + "._delete_workbook")
    @mock.patch(MISTRAL_WBS + "._create_workbook")
    def test_create_delete_workbook(self, mock_create, mock_delete):
        mistral_scenario = workbooks.MistralWorkbooks()
        definition = "---\nversion: \"2.0\"\nname: wb"
        fake_wb = mock.MagicMock()
        fake_wb.name = "wb"
        mock_create.return_value = fake_wb
        mistral_scenario.create_delete_workbook(definition, do_delete=True)

        self.assertEqual(1, mock_create.called)
        mock_delete.assert_called_once_with(fake_wb.name)
