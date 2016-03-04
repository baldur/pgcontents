from notebook.services.sessions.sessionmanager import SessionManager
from .managerbase import PostgresManagerMixin


class PostgresSessionManager(SessionManager):
    @property
    def connection(self):
        """Start a database connection"""
        if self._connection is None:
            self._connection = self.engine
        return self._connection
