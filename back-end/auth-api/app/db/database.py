from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# todo : 환경 변수나, 비밀 파일 패턴으로 보호하길 바람
engine = create_async_engine('postgresql+asyncpg://auth_dev:auth_dev@127.0.0.1/auth')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
