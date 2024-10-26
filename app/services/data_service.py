from flask import jsonify
from sqlalchemy import text
from app.connections.db import Session
from app.data.users_data import users_data
from app.data.products_data import products_data
from app.data.reviews_data import reviews_data
from app.models.users_model import Users
from app.models.product_model import Product
from app.models.review_user_model import Reviews

class DataService: 
    @staticmethod
    def generate_data():
        new_users = []
        with Session() as session:
            try:
                # Check User
                check_users = session.query(Users).count()
                
                # Check Product
                check_products = session.query(Product).count()
                    
                # Check Reviews
                check_reviews = session.query(Reviews).count()
                
                if (check_reviews != 0) or (check_users != 0) or (check_products != 0):
                    return jsonify({
                        "message": "data already exist"
                    }), 400
                    
                # Generate User data
                for user in users_data:
                    new_user: Users = Users(
                        first_name=user["first_name"],
                        last_name=user["last_name"],
                        email=user["email"],
                        gender=user["gender"],
                        birth_date=user["birth_date"],
                        username=user["username"],
                        role=user["role"]
                    )
                    new_user.set_password(user["password"])
                    
                    new_users.append(new_user)
                    
                session.add_all(new_users)
                session.commit()
                
                # Generate Product data
                new_products = [Product(product=product_data["product"],
                                        description=product_data["description"],
                                        price=product_data["price"])
                                for product_data in products_data]
                
                session.add_all(new_products)
                session.commit()
                
                # Generate Review data
                new_reviews = [Reviews(product_id=review["product_id"],
                                       product=review["product"],
                                       description=review["description"],
                                       rating=review["rating"],
                                       user_id=review["user_id"],
                                       username=review["username"])
                               for review in reviews_data]
                
                session.add_all(new_reviews)
                session.commit()
        
                return jsonify({
                    "message": "success generate user, product, and review data"
                }), 201
            except Exception as e:
                session.rollback()
                return jsonify({
                    "message": f"{e}"
                }), 400
                
    @staticmethod
    def show_data():
        with Session() as session:
            try:
                users: Users = session.query(Users).all()
                list_users = [user.to_dict() for user in users]
                
                products: Product = session.query(Product).all()
                list_product = [product.to_dict() for product in products]
                
                reviews: Reviews = session.query(Reviews).all()
                list_reviews = [review.to_dict() for review in reviews]
                
                return jsonify({
                    "message": "success show users",
                    "users": list_users,
                    "products": list_product,
                    "reviews": list_reviews
                }), 200
            except Exception as e:
                return jsonify({
                    "message": f"{e}"
                }), 400
                   
    @staticmethod
    def clear_data():
        with Session() as session:
            try:
                session.query(Reviews).delete()
                session.execute(text("ALTER TABLE reviews AUTO_INCREMENT = 1"))
                session.query(Users).delete()
                session.execute(text("ALTER TABLE users AUTO_INCREMENT = 1"))
                session.query(Product).delete()
                session.execute(text("ALTER TABLE products AUTO_INCREMENT = 1"))
                session.commit()
                
                return jsonify ({
                    "message": "success clear all user, product, and review data"
                }), 200
            except Exception as e:
                session.rollback()
                return jsonify({
                    "message": "failed clear all user, product, and review data"
                }), 400    