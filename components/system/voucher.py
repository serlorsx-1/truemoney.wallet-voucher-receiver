from truemoney.components.http.session import Session


class Voucher:
        def __init__(self, session: Session, hash, count) -> None:
                self.session = session
                
                self.url = '%s%s' % (self.session.paths.template, hash)
                self.hash = hash
                self.count = count

        def redeem(self):
                raw_voucher_redeem = self.session.routes.redeem_voucher(self.hash, self.session.phone)
                if (raw_voucher_redeem.status_code == 200):
                        return True
                
                return False