from src.common import normalize_proxy_uri, get_openray_dedup_key
proxies = [
    "vmess://eyJ2IjoiMiIsInBzIjoiW09wZW5SYXldIER5bmFtaWMtMTA2MzUiLCJhZGQiOiJ6dWxhLmlyIiwicG9ydCI6ODA4MCwiaWQiOiJuYXNuZXQiLCJhaWQiOiIwIiwic2N5IjoiY2hhY2hhMjAtcG9seTEzMDUiLCJuZXQiOiJ3cyIsInR5cGUiOiIiLCJ0bHMiOiIiLCJwYXRoIjoiL25hc25ldC9jZG4iLCJob3N0IjoibmFzbmV0LTUxMTk1MjQyNC5tY2l0ZWwuY28iLCJuYW1lIjoi8J+Hq/Cfh7dGUl8xfDEuM01CL3MifQ==",
    "vmess://eyJhZGQiOiJ6dWxhLmlyIiwiYWlkIjoiMCIsImhvc3QiOiJuYXNuZXQtNTExOTUyNDI0Lm1jaXRlbC5jbyIsImlkIjoibmFzbmV0IiwibmV0Ijoid3MiLCJwYXRoIjoiL25hc25ldC9jZG4iLCJwb3J0IjoiODA4MCIsInNjeSI6ImNoYWNoYTIwLXBvbHkxMzA1IiwidHlwZSI6Im5vbmUiLCJ2IjoiMiJ9"
]
for i,p in enumerate(proxies,1):
    norm = normalize_proxy_uri(p)
    key = get_openray_dedup_key(p)
    print(f"{i} norm: {norm}")
    print(f"{i} key : {key}")
print('unique keys:', len({get_openray_dedup_key(p) for p in proxies}))