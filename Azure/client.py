# -*- coding: utf-8 -*-
# import module snippets
from .base import Base
from .LogAnalytics import *


class Client(Base):
    class LogAnalytics(Base):
        __data_sources: DataSources = None
        __workspaces: Workspaces = None
        __metadata: Metadata = None
        __query: Query = None
        __saved_searches: SavedSearches = None

        @property
        def data_sources(self):
            if self.__data_sources is None:
                self.__data_sources = DataSources(client=self)
            return self.__data_sources

        @property
        def workspaces(self):
            if self.__workspaces is None:
                self.__workspaces = Workspaces(client=self)
            return self.__workspaces

        @property
        def metadata(self):
            if self.__metadata is None:
                self.__metadata = Metadata(client=self)
            return self.__metadata

        @property
        def query(self):
            if self.__query is None:
                self.__query = Query(client=self)
            return self.__query

        @property
        def saved_searches(self):
            if self.__saved_searches is None:
                self.__saved_searches = SavedSearches(client=self)
            return self.__saved_searches

    __log_analytics: LogAnalytics = None

    @property
    def log_analytics(self):
        if self.__log_analytics is None:
            self.__log_analytics = self.__class__.LogAnalytics(client=self)
        return self.__log_analytics
