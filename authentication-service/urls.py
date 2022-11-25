from controllers import Authentication

class UrlPath:
    def __init__(self, resource, route, name):
        self.resource = resource
        self.route = route
        self.name = name

def path(resource, route, name):
    return UrlPath(resource, route, name)

urlpatterns = [
    path(Authentication, "/api/auth/<service>", "authentication")
]