import gnupg

# Ask for gnupg home
gnupghome = input("Enter gnupghome directory(default:/gnupghome): ")

# Set default gnupghome and get gpg object
gpg = gnupg.GPG(gnupghome=gnupghome if gnupghome else '/gnupghome')

import_form = input('Import key from(server/file-path):(default:file-path):: ')

if import_form == 'server':
    key_server = input('Enter key server:: ')
    key_ids = input('Enter key ids(id1 id2 id3 ...)::').split()
    import_result = gpg.recv_keys('server-name', *key_ids)
else:
    key_file = input('Enter keyfile path(default:mykeyfile.asc):: ')

    key_file = key_file if key_file else 'mykeyfile.asc'
    key_data = "".join(open(key_file).readlines())

    import_result = gpg.import_keys(key_data)
print('-------------------- Newly Imported Keys Details-------------------------------------')
print(import_result.__dict__)

print('-------------------------- GPG list of keys -------------------------------')
print('List of public keys::')
print(gpg.list_keys())
print('List of private keys:: ')
print(gpg.list_keys(True))
