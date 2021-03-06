# bip32keys module

This utilities used for generating public / private keys / blockchain address and sign / verify messages.

- `bip32keys` --- library for generating public / private keys / blockchain address
    - `bip32keys` --- contain `Bip32Keys` class which allows generate public / private keys and sign / verify messages
        - `__init__` --- init class with `entropy` or `private_key` parameter
        - `init_from_entropy` --- generate public / private keys based on entropy
        - `init_from_private_key` --- generate public / private keys based on private key
        - `get_public_key` --- return generated public key
        - `get_private_key` --- return generated private key
        - `get_uncompressed_public_key` --- return generated uncompressed public key
        - `sign_msg` --- sign message with private_key
        - `sign_message` --- static function
        - `verify_msg` --- verify message with signature and public_key
        - `verify_message` --- static function
        - `to_uncompressed_public_key` --- convert public key to uncompressed public key
        - `to_compressed_public_key` --- convert uncompressed public key to public key
    - `bip32NetworkKeys` --- contain `Bip32NetworkKeys` class which was based on `Bip32Keys`
        - `__init__` --- init class with `wif` or `entropy` or `private_key` parameter
        - `get_wif` --- return generated wif
        - `wif_to_private_key` --- convert wif to private key
        - `private_key_to_wif` --- convert private key to wif
    - `bip32addresses` --- contain `Bip32Addresses` class which was based on `Bip32NetworkKeys`
        - `__init__` --- init class with `wif` or `entropy` or `private_key` parameter, `magic_byte` parameter should be passed also
        - `get_hex_address` --- return hex address generated based on public key
        - `get_blockchain_address` --- blockchain address generated based on hex address
        - `public_key_to_hex_address` --- convert public key to hex address
        - `hex_address_to_blockchain_address` --- convert hex address to blockchain address
        - `address_to_hex` --- convert address to hex format. Drop magic byte and checksum
        - `is_valid_address` --- check is address valid
        - `get_magic_byte` --- return magic byte
- `qtum_utils` --- packet that contains utils for Qtum
    - `qtum` --- contain class `Qtum` which was based on the `Bip32Addresses`
        - `get_qtum_address` --- return qtum address
        - `hex_to_qtum_address` --- convert hex to qtum address
        - `public_key_to_qtum_address` --- convert public key to qtum address
        - `is_valid_qtum_address` --- check is qtum address valid
- `eth_utuils` --- packet that contains utils for Ethereum
    - `eth` --- contains class `Ethereum` which was based on the `Bip32Keys`
        - `__init__` --- init class
        - `get_address` --- return Ethereum address
        - `public_key_to_ethereum_address` --- convert public key to Ethereum address
- `js_client` --- JavaScript library for working with QTUM (https://qtum.org/en/)
    - `base58` --- parameter alpha is alphabet(currenctly igrone, pass empty string), return encode and decode functions of base58check
    - `privateKeyToWif` - convert private key to wif format
    - `deriveQtumAddress` - get Qtum address from public key
    - `doGenerate` --- generate public, private keys. Should be run in the start!!!
    - `doSign` --- sign message
    - `doVerify` --- verify message

## Installation

Create virtualenv and install needed libraries from the `requirements.txt`:

```bash
cd libs
virtualenv --python=python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
```
