def url_to_hex(url):
    return ''.join(format(ord(char), 'x') for char in url)

url = input("Masukkan URL: ")
hex_url = url_to_hex(url)
print("Berhasil: URL telah diubah menjadi format hex.")
print(hex_url)
