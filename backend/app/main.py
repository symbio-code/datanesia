from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, user, upload, chart, summary, history, payment

app = FastAPI(title="DataNesia Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(upload.router)
app.include_router(chart.router)
app.include_router(summary.router)
app.include_router(history.router)
app.include_router(payment.router)

@app.get("/")
def root():
    return {"message":"DataNesia backend running"}
