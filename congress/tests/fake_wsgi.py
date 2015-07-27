# Copyright (c) 2015 Huawei, Inc. All rights reserved.
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
#

import paste.urlmap

from congress.api import application
from congress.api import versions


def wsgi_app():

    mapper = paste.urlmap.URLMap()
    mapper['/'] = versions.Versions()

    api_resource_mgr = application.ResourceManager()
    api_resource_mgr.register_handler(versions.VersionV1Handler(r'/v1[/]?'))
    app = application.ApiApplication(api_resource_mgr)
    mapper['/v1'] = app

    return mapper
