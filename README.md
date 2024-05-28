# Truemoney Wallet voucher receiver

Used to receive money from voucher link of the truemoney wallet app.

![](https://seeklogo.com/images/T/truemoney-wallet-logo-9CCDDD6CB0-seeklogo.com.png)


#### Example

```python
from client import Client


if (__name__ == '__main__'):
        client = Client('truemoney wallet number')
        client.set_voucher_hash('voucher url')

        voucher = client.get_voucher()
        if (voucher != None):

                result = voucher.redeem()
                if (result):
                        print('Received: %s (%s)' % (
                                voucher.count, voucher.hash
                        ))
```
