from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

import os


# =========================================================
# DATABASE CONFIGURATION
# =========================================================


DATABASE_URL=mysql+pymysql://if0_43049302:VEUPbA3vtQs@sql211.infinityfree.com/if0_43049302_arogya_connect

# =========================================================
# SQLALCHEMY ENGINE
# =========================================================

engine = create_engine(
    DATABASE_URL,

    pool_pre_ping=True,

    pool_recycle=280,

    echo=False
)


# =========================================================
# SESSION
# =========================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# =========================================================
# BASE MODEL
# =========================================================

Base = declarative_base()


# =========================================================
# DATABASE DEPENDENCY
# =========================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()