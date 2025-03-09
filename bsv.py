from bsvlib import Wallet
from bsvlib.constants import Chain
from datetime import datetime, timedelta, timezone

w = Wallet(chain=Chain.MAIN)

w.add_key('jj')
print(w.get_balance(refresh=True))

def lock_bsv_for_2_minutes(wallet, amount_sats):
    lock_time = int((datetime.now(timezone.utc) + timedelta(minutes=2)).timestamp())
    address_to_lock = '1ERc7xAG9oDZtw4a9x7oTGYxz6PLzqfM2Z'
    outputs = [(address_to_lock, amount_sats)]
    tx = wallet.create_transaction(outputs=outputs, lock_time=lock_time)
    return tx.broadcast()

amount_to_lock = 120000  # Amount in satoshis to lock
print(lock_bsv_for_2_minutes(w, amount_to_lock))
