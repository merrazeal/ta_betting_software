from typing import Any


class EsSearchQueryConstuctor:
    def get_base_query(self) -> dict[str, Any]:
        return {
            "query": {"bool": {"must": [], "filter": [], "should": [], "must_not": []}},
            "sort": [],
            "aggs": {},
        }

    def add_pagination(
        self, query: dict[str, Any], page_num: int, page_size: int
    ) -> None:
        query["from"] = (page_num - 1) * page_size
        query["size"] = page_size

    def add_terms_filters(
        self, query: dict[str, Any], filters: list[dict[str, Any]]
    ) -> None:
        for filter in filters:
            query["query"]["bool"]["filter"].append(
                {"terms": {filter["key"]: filter["value"]}}
            )

    def add_must_multi_match_search_query(
        self,
        query: dict[str, Any],
        search_queries: list[dict[str, Any]],
    ) -> None:
        for sq in search_queries:
            query["query"]["bool"]["must"].append(
                {
                    "multi_match": {
                        "query": sq["query"],
                        "fields": sq["fields"],
                    }
                }
            )

    def add_sort(self, query: dict[str, Any], sort: list[dict[str, str]]) -> None:
        for sort_item in sort:
            order = "desc" if sort_item["key"].startswith("-") else "asc"
            field = sort_item["key"].lstrip("-")
            query["sort"].append({field: {"order": order}})

    # ...
