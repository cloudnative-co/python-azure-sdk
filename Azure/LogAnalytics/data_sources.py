# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from ..Utilities.utilities import request_parameter


class DataSources(Base):
    """
    @namespace  Azure.LogAnalytics
    @class      DataSources
    @brief      データソース操作用
    """
    def list(
        self,
        subscription_id: str, resource_group_name: str, workspace_name: str,
        filter: str, api_version: str = "2020-03-01-preview",
        skiptoken: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)
