from sparts.vservice import VService
from sparts.tasks.thrift import NBServerTask
from sparts.tasks.glib import GlibMainLoopTask
from sparts.vfb303 import FacebookBase


class MyGlibEventService(VService, FacebookBase):
    TASKS=[NBServerTask, GlibMainLoopTask]

    def __init__(self, *args, **kwargs):
        VService.__init__(self, *args, **kwargs)
        FacebookBase.__init__(self)


if __name__ == '__main__':
    MyGlibEventService.initFromCLI()
