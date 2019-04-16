# Doc link https://pythonhosted.org/python-gnupg/
import gnupg

# Ask for gnupg home
gnupghome = input("Enter gnupghome directory(default:/gnupghome): ")
# Set default gnupghome and get gpg object
gpg = gnupg.GPG(gnupghome=gnupghome if gnupghome else '/gnupghome')
# Set gpg encoding > default: latin-1
# gpg.encoding = 'utf-8'

data_type = input('Enter data type to encrypt:(text/file): ')

# Using all the keys to encrypt but use specific key(s) and passphrase for more security
keys = [key.get('fingerprint') for key in gpg.list_keys()]
print('Found keys to encrypt: \n', keys)

if data_type == 'text':
    text = input('Enter text: ')
    passphrase = input('Enter passphrase: ')
    encrypted_ascii_data = gpg.encrypt(text, keys, passphrase=passphrase)
    print(encrypted_ascii_data.status)
    print('Encrypted text:: \n', encrypted_ascii_data)
    decrypted_ascii_data = gpg.decrypt(str(encrypted_ascii_data), passphrase=passphrase)
    print(decrypted_ascii_data.status)
    assert str(decrypted_ascii_data) == text
else:
    f_path = input('Enter file path: ')
    passphrase = input('Enter passphrase: ')
    print('Encrypting file:: ', f_path)
    encrypted_file = gpg.encrypt_file(open(f_path, 'rb'), keys, passphrase=passphrase, output=f_path + '_encrypted')
    print(encrypted_file.status)
    print('Decrypting above encrypted file from ', f_path + '_encrypted')
    decrypted_file = gpg.decrypt_file(open(f_path + '_encrypted', 'rb'), passphrase=passphrase, output=f_path + '_decrypted')
    print(decrypted_file.status)
    print('Decrypted file should be same as input file:: \n', "".join(open(f_path + '_decrypted').readlines()))
