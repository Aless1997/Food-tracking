from web3 import Web3
import pprint

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/a65244ad0065445eb502f4474d64b4a3'))
    address = '0x83865320b2F91AD3bb57041337C49027Cf72986b'
    privateKey = '0x7960ca79648864d6a76ff8378f054cd6d1f1dcb3a5cbe340fde29a9eda0b0ac5'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce = nonce,
        gasPrice = gasPrice,
        gas = 100000,
        to = '0x0000000000000000000000000000000000000000',
        value = value,
        data = message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
