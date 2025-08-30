from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routers import auth, analyze, profile, leaderboard, health

app = FastAPI(title='FactForge', version='1.0')

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

@app.on_event('startup')
def startup():
    init_db()

app.include_router(health.router, prefix='/health', tags=['health'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(analyze.router, prefix='/api', tags=['analyze'])
app.include_router(profile.router, prefix='/profile', tags=['profile'])
app.include_router(leaderboard.router, prefix='/leaderboard', tags=['leaderboard'])
