swagger_template = {
    "swagger": "2.0",
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT authorization using the Bearer scheme. Example: 'Authorization: Bearer {token}'"
        }
    }
}