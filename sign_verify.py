# Doc link https://pythonhosted.org/python-gnupg/
import gnupg

# Ask for gnupg home
gnupghome = input("Enter gnupghome directory(default:/gnupghome): ")
# Set default gnupghome and get gpg object
gpg = gnupg.GPG(gnupghome=gnupghome if gnupghome else '/gnupghome')
# Set gpg encoding > default: latin-1
# gpg.encoding = 'utf-8'

data_type = input('Enter data type to sign:(text/file): ')

# Using all the keys to sign but use specific key(s) and passphrase for more security
keys = [key.get('keyid') for key in gpg.list_keys()]
print('Found keys to sign: \n', keys)
print('Using last key of the list: ', keys[-1])

if data_type == 'text':
    text = input('Enter text: ')
    passphrase = input('Enter passphrase: ')
    signed_ascii_data = gpg.sign(text, keyid=keys[-1], passphrase=passphrase)
    print(signed_ascii_data.status)
    print('Signed text:: \n', signed_ascii_data)
    verify_ascii_data = gpg.verify(signed_ascii_data.data)
    assert verify_ascii_data
    print(verify_ascii_data.status)
else:
    f_path = input('Enter file path: ')
    passphrase = input('Enter passphrase: ')
    print('Signing file:: ', f_path)
    signed_file = gpg.sign_file(open(f_path, 'rb'), keys[-1], passphrase=passphrase, output=f_path + '_signed')
    print(signed_file.status)
    verify_file = gpg.verify_file(open(f_path + '_signed', 'rb'))
    print(verify_file.status)
