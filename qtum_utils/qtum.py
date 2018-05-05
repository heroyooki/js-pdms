from bip32keys.bip32addresses import Bip32Addresses


class Qtum(Bip32Addresses):

    def __init__(self, init_params, mainnet=True):
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
    q = Qtum("89324890413289043287943127894312789431241324132431243", mainnet=False)
    print('private key: ' + q.get_private_key())
    print('wif: ' + q.get_wif())
    print('public key: ' + q.get_public_key())
    print('uncompressed public key: ' + q.get_uncompressed_public_key())
    print('qtum address: ' + q.get_qtum_address())
    print('qtum hex address: ' + q.get_hex_address())


def test_signature():

    q = Qtum('894389032980328902980324089324432432234324234', mainnet=False)
    public_key = q.get_uncompressed_public_key()
    private_key = q.get_private_key()
    message = 'hello'

    signature = Qtum.sign_message(message, private_key)
    print(Qtum.verify_message(message, signature, public_key))


if __name__ == '__main__':
    test_address()
    test_signature()
