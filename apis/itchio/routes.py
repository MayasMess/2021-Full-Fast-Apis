from apis.itchio.itchio import Itchio
from apis import router
from fastapi_utils.cbv import cbv


@cbv(router)
class ItchioRoutes(Itchio):
    def __init__(self):
        super().__init__()

    @router.get("/itchio")
    async def root(self):
        return {"message": self.welcome_msg}
