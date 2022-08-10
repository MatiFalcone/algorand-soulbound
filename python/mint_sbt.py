import json
from algosdk import constants
from algosdk.v2client import algod
from algosdk.future import transaction


def mint_sbt_example(private_key, my_address):
    
    # Connect to node
    algod_client = algod.AlgodClient(algod_token, algod_address, headers)

    # Get account information
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

    # Build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE

    metadata_json = {
        "standard": "ARC5114",
        "status": "issued",
        "description": "ARC5114 Membership Card",
        "mime_type": "image/png"
    }
    json_data = json.dumps(metadata_json)
    json_hex = "7b227374616e64617264223a202241524335313134222c202273746174757322"

    try:
        unsigned_txn = transaction.AssetConfigTxn(
            sender=my_address,
            sp=params,
            total=1,
            default_frozen = False,
            unit_name = "ARC5114",
            asset_name = "ARC5114 Membership Card",
            manager = my_address,
            reserve = "",
            freeze = my_address,
            clawback = my_address,
            url = "ipfs://QmepNYKTRQQDeeogGbYTBLUUi7YyxEE3KHngFRkJCMG7rZ",
            metadata_hash = bytes.fromhex(json_hex),
            strict_empty_address_check=False,
            note = json_data.encode(),
            decimals = 0)
    except Exception as err:
        print(err)
        return

    # Sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # Submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")