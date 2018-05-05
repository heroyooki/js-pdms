from bip32keys.bip32addresses import Bip32Addresses


class Qtum(Bip32Addresses):

    def __init__(self, init_params, mainnet):
        super().__init__(init_params, Qtum._get_magic_byte(mainnet), mainnet)

    def get_qtum_address(self):
        return super().get_blockchain_address()

    @staticmethod
    def hex_to_qtum_address(hex_address, mainnet):
        return Bip32Addresses.hex_address_to_blockchain_address(hex_address, Qtum._get_magic_byte(mainnet))

    @staticmethod
    def _get_magic_byte(mainnet):
        if mainnet:
            return '3a'
        else:
            return '78'


def test_address():
    q = Qtum("3123213213213123312c3kjifj3", mainnet=False)
    print('private key: ' + q.get_private_key())
    print('wif: ' + q.get_wif())
    print('public key: ' + q.get_public_key())
    print('uncompressed public key: ' + q.get_uncompressed_public_key())
    print('qtum address: ' + q.get_qtum_address())
    print('qtum hex address: ' + q.get_hex_address())
    print('my wif: ' + Qtum.private_key_to_wif('7a6be1df9cc5d88edce5443ef0fce246123295dd82afae9a57986543272157cc', mainnet=False))
    print('wif to private key: ' + Qtum.wif_to_private_key('L1KgWtY57mSggocxDVSDRGvLVCRYuQfj8ur7cHvuv6UkgJmXweti'))

    print('hex_address: ', Qtum.address_to_hex('qHmBaB5dWsxWtMh3MNh6B427L47DWavgJD'))
    print('qtum address: ', Qtum.hex_to_qtum_address('023b5269b46be13e6ac5c3f122ed263e9fa78114', mainnet=False))


def test_signature():

    q = Qtum('1232131234324324324234321231', mainnet=False)
    public_key = q.get_uncompressed_public_key()
    private_key = q.get_private_key()
    message = 'hello'

    signature = Qtum.sign_message(message, private_key)
    print(Qtum.verify_message(message, signature, public_key))


if __name__ == '__main__':
    test_address()
    test_signature()