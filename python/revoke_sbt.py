import json
from algosdk import constants
from algosdk.v2client import algod
from algosdk.future import transaction


def revoke_sbt_example(sbt_asset_id, claimer_account, claimer_private_key, issuer_account, issuer_private_key):

    # Connect to node
    algod_client = algod.AlgodClient(algod_token, algod_address, headers)

    # Get account information
    account_info = algod_client.account_info(claimer_account)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

    # Get network params
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE

    # 1) Issuer unfreezes SBT transaction
    try:
        unfreeze_txn = transaction.AssetFreezeTxn(
            sender=issuer_account,
            sp=params,
            index=sbt_asset_id,
            target=claimer_account,
            new_freeze_state=False)
    except Exception as err:
        print(err)
        return

    # 2) Issuer updates the metadata of the transaction
    metadata_json = {
        "standard": "ARC5114", 
        "status": "revoked", 
        "description": "ARC5114 Membership Card",
        "mime_type": "image/png"
    }
    json_data = json.dumps(metadata_json)

    try:
        update_txn = transaction.AssetConfigTxn(
            sender=issuer_account,
            sp=params,
            index=sbt_asset_id,
            note=json_data.encode(),
            manager=issuer_account,
            reserve="",
            freeze=issuer_account,
            clawback=issuer_account,
            strict_empty_address_check=False)
    except Exception as err:
        print(err)
        return

    # 3) Issuer clawbacks SBT from claimer's account
    try:
        clawback_txn = transaction.AssetTransferTxn(
            sender=claimer_account,
            sp=params,
            receiver=issuer_account,
            amt=1,
            index=sbt_asset_id,
            revocation_target=claimer_account
        )
    except Exception as err:
        print(err)
        return

    # Group transactions together for Atomic Transfer
    gid = transaction.calculate_group_id([unfreeze_txn, update_txn, clawback_txn])
    unfreeze_txn.group = gid
    update_txn.group = gid
    clawback_txn.group = gid

    # Sign the transactions individually
    sunfreeze_txn = unfreeze_txn.sign(issuer_private_key)
    supdate_txn = update_txn.sign(issuer_private_key)
    sclawback_txn = clawback_txn.sign(issuer_private_key)

    # Assemble transaction group
    signed_group = [sunfreeze_txn, supdate_txn, sclawback_txn]

    # Submit transaction
    txid = algod_client.send_transactions(signed_group)
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