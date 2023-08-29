# http://www.pythonchallenge.com/pc/return/evil.html

types = {
	b'\xFF\xD8\xFF': '.jpg',
	b'\x89\x50\x4E\x47': '.png',
	b'\x47\x49\x46\x38': '.gif',
}

with open('evil2.gfx', 'rb') as evil:
	evil_bytes = [[] for _ in range(5)]
	for i, byte in enumerate(evil.read()):
		evil_bytes[i % 5].append(byte)
  
	for i, evil_byte in enumerate(evil_bytes):
		for byte, ex in types.items():
			if bytes(evil_byte).startswith(byte):
				with open(f'evil_gfx/evil-{i}{ex}', 'wb') as f:
					f.write(bytes(evil_byte))