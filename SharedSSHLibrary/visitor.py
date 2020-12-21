from robot.api import logger
from robot.model import SuiteVisitor

from SharedSSHLibrary.singleton import Singleton


class SSHLibraryModifier(SuiteVisitor):

    def start_suite(self, suite):
        if suite.parent is None:
            return

        from SSHLibrary import SSHLibrary
        from SSHLibrary.sshconnectioncache import SSHConnectionCache

        @Singleton
        class SharedSSHConnectionCache(SSHConnectionCache):
            pass

        def __init__(self, *args, **kwargs):
            SSHLibrary.__init_base__(self, *args, **kwargs)
            self._connections = SharedSSHConnectionCache()

        SSHConnectionCache = SharedSSHConnectionCache

        SSHLibrary.__init_base__ = SSHLibrary.__init__
        SSHLibrary.__init__ = __init__

        logger.console(f"""""")
