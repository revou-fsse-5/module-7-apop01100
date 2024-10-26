from app.connections.db import Base
from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, nullable=False)
    product = Column(String(128), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(DECIMAL(16, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=None, onupdate=datetime.now(timezone.utc), nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    
    # Relationship Table
    # reviews_relation = relationship("Reviews", back_populates="products")
    
    def to_dict(self):
        product_item = {
            "id": self.id,
            "product": self.product,
            "description": self.description,
            "metadata": {
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "is_deleted": self.is_deleted  
            }
        }
        
        return product_item