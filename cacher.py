import datetime
import subprocess
import os
import sys


UPDATE_PERIOD_SECONDS = 600


def get_last_time() -> int:
    try:
        seconds_cached = open("cache/last_recheck.int", 'rb')
    except:
        return 0

    try:
        result = seconds_cached.read()
        result = int.from_bytes(result, byteorder='little')
    except:
        return 0
    finally:
        seconds_cached.close()

    return result


def set_last_time(new_unix_time: int):
    seconds_cached = open("cache/last_recheck.int", 'wb')
    seconds_cached.write(new_unix_time.to_bytes(4, byteorder='little'))
    seconds_cached.close()


def get_last_charge() -> str:
    try:
        charge_cached = open("cache/last_charge.txt", 'r')
    except:
        return ''

    try:
        result = charge_cached.read().rstrip('\r\n')
    except:
        return ''
    finally:
        charge_cached.close()

    return result


def set_last_charge(charge: str):
    charge_cached = open("cache/last_charge.txt", 'w')
    charge_cached.write(charge.rstrip('\r\n'))
    charge_cached.close()


def main():
    os.makedirs("cache", exist_ok=True)
    if len(sys.argv) < 2:
        return
    unix_time = int(datetime.datetime.utcnow().timestamp())
    last_unix_time = get_last_time()
    charge = get_last_charge()
    if (len(sys.argv) > 2 and sys.argv[2] == "force-refresh") or (unix_time - last_unix_time) > UPDATE_PERIOD_SECONDS:
        set_last_time(unix_time)
        proc = subprocess.Popen(args=['./get_charge_immediately.sh', sys.argv[1]], stdout=subprocess.PIPE)
        charge = proc.stdout.read().decode()
        set_last_charge(charge)
    print(charge)


if __name__ == "__main__":
    main()
