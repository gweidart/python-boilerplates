from tg import expose, TGController

class RootController(TGController):
    @expose('project_name.templates.welcome')
    def index(self):
        return dict(message="Welcome to TurboGears!")
