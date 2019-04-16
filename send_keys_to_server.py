# Doc link https://pythonhosted.org/python-gnupg/
import gnupg

# Ask for gnupg home
gnupghome = input("Enter gnupghome directory(default:/gnupghome): ")
# Set default gnupghome and get gpg object
gpg = gnupg.GPG(gnupghome=gnupghome if gnupghome else '/gnupghome')
# Set gpg encoding > default: latin-1
gpg.encoding = 'utf-8'

# Set key server
server_name = input('Enter key server hostname(default:keyserver.ubuntu.com):: ')
keyserver = server_name if server_name else 'keyserver.ubuntu.com'
# Send keys to server
for key in gpg.list_keys():
    response = gpg.send_keys(keyserver, key.get('keyid'))
    print('Key:: ', key, '\nResponse:: ', response.__dict__)

# Verify by searching keys from server
print('------------------:: Searching for keys:: -----------------------')
keyids = [key.get('keyid') for key in gpg.list_keys()]
print('Key server:: ', keyserver, '\nKeyids:: ', keyids)
# Verify and search key
keys_found = gpg.recv_keys(keyserver, *keyids)
print('-----------------------:: Found ::---------------------- \n', keys_found.__dict__)
