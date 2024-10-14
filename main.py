from fastapi import FastAPI
import hvac
import os

app = FastAPI()

client = hvac.Client(url=os.getenv('VAULT_ADDR'))
client.token = os.getenv('VAULT_TOKEN')

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Vault integration"}

@app.get("/secret/{key}")
def read_secret(key: str):
    if client.is_authenticated():
        secret = client.secrets.kv.v2.read_secret_version(path=key)
        return {"secret": secret['data']['data']}
    return {"error": "Vault authentication failed"}