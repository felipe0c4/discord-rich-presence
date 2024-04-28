from pypresence import Presence
import time
import os

client_id = # id
RPC = Presence(client_id)
RPC.connect()
open_time_m = -1
open_time_h = 0
start_time = int(time.time())

while True:
    RPC.update(
        large_image=" assets ",
        details =" details ",
        start=start_time,
        buttons=[{"label": "Follow me", "url": "https://github.com/felipe0c4"}]
    )
    os.system("cls")
    open_time_m += 1

    if open_time_m >= 60:
        open_time_h += 1
        open_time_m -= 60
    print("RPC ativo a: ", open_time_h, "horas e", open_time_m, "minutos")
    time.sleep(60)
