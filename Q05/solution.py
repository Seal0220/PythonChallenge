import pickle

with open('banner.p', 'r') as banner:
    banner_pickle = pickle.loads(banner.read().encode())
    print(banner_pickle)

for li in banner_pickle:
    for t in li:
        print(''.join([t[0] for _ in range(t[1])]), end='')
        
    print()
    