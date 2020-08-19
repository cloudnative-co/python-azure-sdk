Maps = {
    "DataSources": {
        "list": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataSources",
            "query": """{{
                "$filter": {filter},
                "api-version": {api_version},
                "$skiptoken": {skiptoken}
            }}"""
        }
    },
    "Azure.LogAnalytics.metadata.Metadata": {
        "get": {
            "method": "GET",
            "url": "https://api.loganalytics.io/v1/workspaces/{workspace_id}/metadata"
        },
        "post": {
            "method": "POST",
            "url": "https://api.loganalytics.io/v1/workspaces/{workspace_id}/metadata"
        }
    },
    "Azure.LogAnalytics.query.Query": {
        "execute": {
            "method": "POST",
            "url": "https://api.loganalytics.io/v1/workspaces/{workspace_id}/query",
            "payload": """{{
                "query": {query},
                "timespan": {timespan},
                "workspaces": {workspaces}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://api.loganalytics.io/v1/workspaces/{workspace_id}/query",
            "query": """{{
                "query": {query},
                "timespan": {timespan}
            }}"""
        }
    },
    "Azure.LogAnalytics.saved_searches.SavedSearches": {
        "list": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/savedSearches",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/savedSearches/{saved_search_id}",
            "query": """{{
                "api-version": {api_version}
            }}"""
        }
    },
    "Azure.LogAnalytics.workspaces.Workspaces": {
        "available_service_tiers": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/availableServiceTiers",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "create": {
            "method": "PUT",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "clusters": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/clusters",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "data_exports": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataExports",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "data_sources": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataSources",
            "query": """{{
                "$filter": {filter},
                "api-version": {api_version},
                "$skiptoken": {skiptoken}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.OperationalInsights/workspaces",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "list_by_resource_group": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "regenerate_shared_key": {
            "method": "POST",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/regenerateSharedKeys",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "schema": {
            "method": "POST",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/schema",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "shared_key": {
            "method": "POST",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/sharedKeys",
            "query": """{{
                "api-version": {api_version}
            }}"""
        },
        "usage": {
            "method": "GET",
            "url": "https://management.azure.com/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/usages",
            "query": """{{
                "api-version": {api_version}
            }}"""
        }
    }
}
