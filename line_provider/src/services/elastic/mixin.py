from common.schemas import BaseEsParams


class ListMixinEsService:

    def get_list_query(self, params: BaseEsParams):
        query = self.es_search_constructor.get_base_query()
        self.es_search_constructor.add_pagination(
            query, params.pagination.page_number, params.pagination.page_size
        )
        self.es_search_constructor.add_terms_filters(query, params.terms_filters)
        self.es_search_constructor.add_sort(query, params.sort)
        self.es_search_constructor.add_must_multi_match_search_query(
            query, params.must_multimatch_search_query
        )
        return query
