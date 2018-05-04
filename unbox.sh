# Create a new virtualenv in a hidden directory.  
python3 -m venv .env

# Activate the sandbox.  
source .env/bin/activate

# Install requirements from the sandbox (remember to run `pip3 freeze > requirements.txt` regularly)
pip3 install -r requirements.txt