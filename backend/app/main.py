from fastapi import FastAPI

app = FastAPI(
    title="ShieldID Provider",
    description="Decentralized Identity and Credential Issuer",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message" : "ShieldID API is running"}

