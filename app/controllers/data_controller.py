from flask import request
from app.services.data_service import DataService

def data_controller():
    if request.method == "GET":
        response = DataService.show_data()
        
        return response
    
    if request.method == "POST":
        response = DataService.generate_data()
        
        return response
    
    if request.method == "DELETE":
        response = DataService.clear_data()
        
        return response