# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from ..Utilities.utilities import request_parameter
from .collector import Collector


class Workspaces(Base):
    """
    @namespace  Azure.LogAnalytics
    @class      Workspaces
    @brief      Workspaces操作用
    """

    def available_service_tiers(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        ワークスペースで使用可能なサービスレベルを取得します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def create(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        ワークスペースを作成または更新します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def data_exports(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        ワークスペース内のデータエクスポートインスタンスを一覧表示します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, subscription_id: str, api_version: str = "2020-03-01-preview"
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list_by_resource_group(
        self, resource_group_name: str, subscription_id: str,
        api_version: str = "2020-03-01-preview"
    ):
        request = request_parameter(locals())
        return self.http_request(**request)


    def schema(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def shared_key(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        ワークスペースの共有キーを取得します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def regenerate_shared_key(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        ワークスペースの共有キーを再取得します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def usage(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str, api_version: str = "2020-03-01-preview"
    ):
        """
        ワークスペースの共有キーを取得します。
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def collector(
        self, resource_group_name: str, subscription_id: str,
        workspace_name: str
    ):
        ws_info = self.get(resource_group_name, subscription_id, workspace_name)
        ky_info = self.shared_key(resource_group_name, subscription_id, workspace_name)
        workspace_id = ws_info["properties"]["customerId"]
        shared_key = ky_info["primarySharedKey"]
        collector = Collector(workspace_id, shared_key)
        return collector
