from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base
import enum

class Role(str, enum.Enum):
    customer = "customer"
    driver = "driver"
    admin = "admin"

class VerificationStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.customer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DriverDocument(Base):
    __tablename__ = "driver_documents"
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String, nullable=False)
    doc_type = Column(String, nullable=False)  # license, id_card, photo
    status = Column(Enum(VerificationStatus), default=VerificationStatus.pending, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
