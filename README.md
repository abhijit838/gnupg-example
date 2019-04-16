Gnupg Exapmle
-----------------
#### Setup:
```bash
apt-get update && \
pip install python-gnupg && \
mkdir /gnupghome
```
Or install Docker and run below command
```bash
docker build -t mygnupg .
docker run --rm -it mygnupg bash
```

#### Use Gnupg
```bash
python <script-name>
```