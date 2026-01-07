from src.common import normalize_proxy_uri, get_openray_dedup_key
proxies = [
"trojan://87d1bfd4-574e-4c96-ad42-0426f27461ff@cf.090227.xyz:443?path=%2F&security=tls&host=_acme-challenge.2go.cloudns.be&type=ws&sni=_acme-challenge.2go.cloudns.be&allowInsecure=1#%5BOpenRay%5D%20Dynamic-8530",
"trojan://87d1bfd4-574e-4c96-ad42-0426f27461ff@cf.090227.xyz:443?security=tls&sni=_acme-challenge.2go.cloudns.be&type=ws&path=/?ed=2560&Host=_acme-challenge.2go.cloudns.be#%5BOpenRay%5D%20Dynamic-7591"


]
for i,p in enumerate(proxies,1):
    norm = normalize_proxy_uri(p)
    key = get_openray_dedup_key(p)
    print(f"{i} norm: {norm}")
    print(f"{i} key : {key}")
print('unique keys:', len({get_openray_dedup_key(p) for p in proxies}))