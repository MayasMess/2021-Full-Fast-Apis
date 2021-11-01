from apis.linkedin.linkedin import Linkedin
from apis import router
from fastapi_utils.cbv import cbv


@cbv(router)
class LinkedinRoutes(Linkedin):
    def __init__(self):
        super().__init__()

    @router.get("/linkedin/user-info/{slug}")
    async def linkedin_user_info(self, slug: str) -> dict:
        return self.retrieve_linkedin_user_info(slug=slug)
