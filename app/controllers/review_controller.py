from flask import jsonify, request
from pydantic import ValidationError
from app.services.review_service import ReviewsService
from app.utils.review_validation import ReviewValidation
from app.utils.role_required import role_required
from flasgger import swag_from

@role_required("admin")
@swag_from("../docs/review_admin_api_doc.yaml")
def reviews_controller():
    if request.method == "GET":
        response = ReviewsService.show_reviews()
        return response
    
@role_required("user")
def create_user_review_controller():
    data = request.json
    
    try:
        review_valid = ReviewValidation.model_validate(data)
    except ValidationError as e:
        return jsonify({
            "message": f"{e}"
        })
    
    response = ReviewsService.create_review(review_valid.model_dump())
    
    return response