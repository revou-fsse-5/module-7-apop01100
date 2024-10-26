from flask import jsonify
from sqlalchemy import text
from app.connections.db import Session
from app.data.reviews_data import reviews_data
from app.models.product_model import Product
from app.models.review_user_model import Reviews
from app.models.users_model import Users

class ReviewsService:                 
    @staticmethod
    def show_reviews():
        with Session() as session:
            try:
                reviews: Reviews = session.query(Reviews).all()
                list_reviews = [review.to_dict() for review in reviews]
                return jsonify({
                    "message": "success show reviews",
                    "products": list_reviews
                }), 200
            except Exception as e:
                return jsonify({
                    "message": f"{e}"
                }), 400
                
    @staticmethod
    def create_review(data):
        with Session() as session:
            try:
                check_user_id: Users = session.query(Users).filter(Users.username == data["username"]).first()
                check_product_id: Product = session.query(Product).filter(Product.product == data["product"]).first()
                
                if check_user_id is None and check_product_id is None:
                    return jsonify({
                        "message": "user_id or product_id not exist"
                    }), 400
                    
                new_review = Reviews(product_id=check_product_id.id,
                                     product=data["product"],
                                     description=data["description"],
                                     rating=data["rating"],
                                     user_id=check_user_id.id,
                                     username=data["username"])
                
                session.add(new_review)
                session.commit()
                return jsonify({
                    "message": "success get reviews user data"
                }), 201
            except Exception as e:
                return jsonify({
                    "message": f"{e}"
                }), 400