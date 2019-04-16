# Doc link https://pythonhosted.org/python-gnupg/
import gnupg

# Ask for gnupg home
gnupghome = input("Enter gnupghome directory(default:/gnupghome): ")
# Set default gnupghome and get gpg object
gpg = gnupg.GPG(gnupghome=gnupghome if gnupghome else '/gnupghome')
# Set gpg encoding > default: latin-1
# gpg.encoding = 'utf-8'

# Find keys
keys = [key.get('fingerprint') for key in gpg.list_keys()]
print('Found keys: \n', keys)

passphrase = input('Enter passphrase: ')

# Delete keys
for key in keys:
    # delete public key
    gpg.delete_keys(key, passphrase=passphrase)
    # delete private key
    gpg.delete_keys(key, passphrase=passphrase, secret=True)
    print('Deleted key: ', key)
