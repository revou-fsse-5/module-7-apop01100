from app.connections.db import Base
from sqlalchemy import Column, ForeignKey, Integer, Text, CheckConstraint, String
from sqlalchemy.orm import relationship

class Reviews(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    username = Column(String(128), nullable=False)
    
    # Relationship Table
    # product = relationship("Product", back_populates="reviews")
    # users = relationship("Users", back_populates="reviews")
    
    __table_args__  = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="rating_range"),
    )
    
    def to_dict(self):
        review = {
            "id": self.id,
            "product_id": self.product_id,
            "product": self.product,
            "description": self.description,
            "rating": self.rating,
            "user_id": self.user_id,
            "username": self.username
        }
        
        return review
    
    