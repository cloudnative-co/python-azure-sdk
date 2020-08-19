# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from ..Utilities.utilities import request_parameter


class Metadata(Base):
    """
    @namespace  Azure.LogAnalytics.metadata
    @class      Metadata
    @brief      メタデータ操作用
    """

    def get(self, workspace_id: str):
        request = request_parameter(locals())
        return self.http_request(**request)

    def post(self, workspace_id: str):
        request = request_parameter(locals())
        return self.http_request(**request)
