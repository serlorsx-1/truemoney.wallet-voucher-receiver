from truemoney.components.http.paths import Paths
from truemoney.components.http.route import Routes

from curl_cffi.requests.session import Session


class Session(Session):
        paths = Paths

        def __init__(self) -> None:
                super().__init__()

                self.routes = Routes(self)
                self.headers.update({
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
                })