from httpx import Client


class Routes:
        def __init__(self, session: Client) -> None:
                self.session = session

        def voucher_verify(self, code):
                return self.session.get('%s/%s/verify' % (self.session.paths.base_url, code))
        
        def redeem_voucher(self, code, phone):
                return self.session.post('%s/%s/redeem' % (self.session.paths.base_url, code), json={'mobile': phone, 'voucher_hash': code})