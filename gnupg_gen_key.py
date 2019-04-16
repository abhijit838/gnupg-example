# Doc link https://pythonhosted.org/python-gnupg/
import gnupg

# Ask for gnupg home
gnupghome = input("Enter gnupghome directory(default:/gnupghome): ")
# Set default gnupghome and get gpg object
gpg = gnupg.GPG(gnupghome=gnupghome if gnupghome else '/gnupghome')
# Set gpg encoding > default: latin-1
gpg.encoding = 'utf-8'

# Key input data
key_name_email = input('Enter email: ')
key_type = input('Enter key type(default:RSA):')
key_length = input('Enter key length:(default:1024)')
passphrase = input('Enter passphrase: ')

# Preparing key input parameters
input_data = gpg.gen_key_input(
    name_email=key_name_email,
    key_type=key_type if key_type else 'RSA',
    key_length=int(key_length) if key_length else 1024,
    passphrase=passphrase)

# Generating key
key = gpg.gen_key(input_data)

# Print key fingerprint
print('Generated key(fingerprint): ', key)
# Export public key
ascii_armored_public_keys = gpg.export_keys(str(key), passphrase=passphrase)
print('Exported public key: \n', ascii_armored_public_keys)
# Export private key
ascii_armored_private_keys = gpg.export_keys(str(key), True, passphrase=passphrase)
print('Exported private key: \n', ascii_armored_private_keys)

export_file = input('Export file path:(default:mykeyfile.asc):')
export_file = export_file if export_file else 'mykeyfile.asc'
# Save keys in a file
with open(export_file, 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)

print('Hurray !!! your exported key(s) at > ', export_file)

print('---------------------------- GPG list of keys -------------------------------')
print('List of public keys::\n')
print(gpg.list_keys())
print('List of private keys:: \n')
print(gpg.list_keys(True))
