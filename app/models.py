from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IP(Base):
    __tablename__ = "ips"
    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String(45), unique=True, nullable=False)
    country = Column(String(100))
    abuse_score = Column(Integer)
    report_count = Column(Integer)
    last_reported_at = Column(TIMESTAMP)
    ml_prediction = Column(String(50))
    created_at = Column(TIMESTAMP)

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    ip_input = Column(String(45), nullable=False)
    user_agent = Column(String)
    ip_id = Column(Integer, ForeignKey("ips.id"))
    created_at = Column(TIMESTAMP)
