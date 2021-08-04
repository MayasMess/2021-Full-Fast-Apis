from apis.itchio.itchio import Itchio
from apis import router
from fastapi_utils.cbv import cbv


@cbv(router)
class ItchioRoutes(Itchio):
    def __init__(self):
        super().__init__()

    @router.get("/itchio/recent-uploads/{page_num}")
    async def itchio(self, page_num: int):
        self.retrieve_new_game_uploads(page_num=page_num)
        return self.results
