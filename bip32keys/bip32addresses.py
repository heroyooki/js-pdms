
from bip32keys.bip32NetworkKeys import Bip32NetworkKeys, encode_hex, decode_hex
from hashlib import sha256
import hashlib
import base58check


class Bip32Addresses(Bip32NetworkKeys):

    def __init__(self, init_params, magic_byte, mainnet=True):
        super().__init__(init_params, mainnet)
        self.hex_address = Bip32Addresses.public_key_to_hex_address(self.get_public_key())
        self.blockchain_address = Bip32Addresses.hex_address_to_blockchain_address(self.hex_address, magic_byte)

    def get_hex_address(self):
        return self.hex_address

    def get_blockchain_address(self):
        return self.blockchain_address

    @staticmethod
    def public_key_to_hex_address(public_key):
        public_key = Bip32Addresses.to_compressed_public_key(public_key)

        output = sha256(decode_hex(public_key)[0]).digest()

        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(output)
        output = ripemd160.hexdigest()

        return output

    @staticmethod
    def hex_address_to_blockchain_address(hex_address, mb):

        output = mb + hex_address
        extended_ripemd160 = output

        output = decode_hex(output)[0]

        checksum = sha256(sha256(output).digest()).hexdigest()[:8]

        output = extended_ripemd160 + checksum

        output = decode_hex(output)[0]
        output = base58check.b58encode(output)
        return output.decode()

    @staticmethod
    def address_to_hex(address):
        output = encode_hex(base58check.b58decode(address))[0]

        return output[2:-8].decode()  # drop magic byte and checksum


if __name__ == '__main__':
    keys = Bip32Addresses({'wif': 'cRgfyoXvYq8wrF6DbuFLnbRQ7RixZrmRCwzaiiPRRD8kw3qxwqxi'}, mainnet=False, magic_byte='78')

    print('public key: ', keys.get_public_key())
    print('private key: ', keys.get_private_key())
    print('uncompressed public key: ', keys.get_uncompressed_public_key())
    print('wif: ', keys.get_wif())
    print('address: ', keys.get_hex_address())
    print('address: ', keys.get_blockchain_address())
