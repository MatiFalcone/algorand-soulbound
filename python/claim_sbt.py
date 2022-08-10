import json
from algosdk import constants
from algosdk.v2client import algod
from algosdk.future import transaction


def claim_sbt_example(sbt_asset_id, claimer_account, claimer_private_key, issuer_account, issuer_private_key):

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

    # 1) Build SBT opt-in transaction
    try:
        optin_txn = transaction.AssetTransferTxn(
            sender=claimer_account,
            sp=params,
            receiver=claimer_account,
            amt=0,
            index=sbt_asset_id)
    except Exception as err:
        print(err)
        return

    # 2) Issuer updates the metadata to reflect status as "claimed"
    metadata_json = {
        "standard": "ARC5114", 
        "status": "claimed", 
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

    # 3) Issuer sends SBT to claimer's account
    try:
        send_txn = transaction.AssetTransferTxn(
            sender=issuer_account,
            sp=params,
            receiver=claimer_account,
            amt=1,
            index=sbt_asset_id)
    except Exception as err:
        print(err)
        return

    # 4) Issuer freezes SBT
    try:
        freeze_txn = transaction.AssetFreezeTxn(
            sender=issuer_account,
            sp=params,
            index=sbt_asset_id,
            target=claimer_account,
            new_freeze_state=True)
    except Exception as err:
        print(err)
        return

    # Group transactions together for Atomic Transfer
    gid = transaction.calculate_group_id([optin_txn, update_txn, send_txn, freeze_txn])
    optin_txn.group = gid
    update_txn.group = gid
    send_txn.group = gid
    freeze_txn.group = gid

    # Sign the transactions individually
    soptin_txn = optin_txn.sign(claimer_private_key)
    supdate_txn = update_txn.sign(issuer_private_key)
    ssend_txn = send_txn.sign(issuer_private_key)
    sfreeze_txn = freeze_txn.sign(issuer_private_key)

    # Assemble transaction group
    signed_group = [soptin_txn, supdate_txn, ssend_txn, sfreeze_txn]

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