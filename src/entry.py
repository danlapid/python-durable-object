from workers import Response, handler, DurableObject

class DurableObjectExample(DurableObject):
    def __init__(self, state, env):
        super().__init__(state, env)

    async def greet(self):
        result = self.ctx.storage.sql.exec("SELECT 'Hello, World!' as greeting").one()
        return result.greeting


@handler
async def on_fetch(request, env):
    id = env.ns.idFromName("A")
    obj = env.ns.get(id)

    return Response(await obj.greet())
