# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from ..Utilities.utilities import request_parameter


class SavedSearches(Base):
    """
    @namespace  Azure.LogAnalytics
    @class      SavedSearches
    @brief      保存された検索条件用
    """

    def list(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        指定された Log Analytics ワークスペースの保存された検索条件を取得します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, resource_group_name: str, save_search_id: str,
        subscription_id: str, workspace_name: str,
        api_version: str = "2020-03-01-preview"
    ):
        request = request_parameter(locals())
        return self.http_request(**request)
