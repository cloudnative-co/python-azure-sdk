# -*- coding: utf-8 -*-
# import module snippets
from .exception import LogAnalyticsDataAccessException
from ..base import Base
from ..Utilities.utilities import request_parameter


class Query(Base):
    """
    @namespace  Azure.LogAnalytics
    @class      Query
    @brief      クエリ―実行用
    """

    def execute(
        self, workspace_id: str, query: str, timespan: str = None,
        workspaces: list = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, workspace_id: str, query: str, timespan: str = None
    ):
        request = request_parameter(locals())
        result = self.http_request(**request)
        if "error" in result:
            raise LogAnalyticsDataAccessException(result["error"])
        return result
