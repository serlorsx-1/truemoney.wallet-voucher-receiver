from truemoney.components.http.session import Session
from truemoney.components.system.voucher import Voucher


class Client(Session):
        def __init__(self, phone) -> None:
                super().__init__()

                self.phone = phone
                self.hash = None
        
        def extract_voucher(self, url):
                return url.split(self.paths.template, 1)[1]

        def set_voucher_hash(self, url):
                if (self.paths.template in url):
                        self.hash = self.extract_voucher(url)

        def get_voucher(self):
                if (self.hash != None):
                        raw_voucher_data = self.routes.voucher_verify(self.hash)

                        if (raw_voucher_data.status_code == 200):
                                data = raw_voucher_data.json()
                                data = data['data'].get('voucher')

                                sum_baht = int(float(data.get('amount_baht')))
                                member_count = int(data.get('member'))

                                voucher = Voucher(self, self.hash, sum_baht // member_count)
                                
                                return voucher