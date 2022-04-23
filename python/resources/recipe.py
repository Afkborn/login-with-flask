from http import HTTPStatus
from flask_restful import Resource
from flask import request

from python.UserDatabase import Database
from python.model.User import User



    
class UserRecipe(Resource):
    myDb = Database()
    def get(self, username):
        user = self.myDb.getUserWithUsername(username)
        if user is None:
            return {
                "status": HTTPStatus.NOT_FOUND,
                'message': 'User not found!'}

        return {
            "status": HTTPStatus.OK,
            'user': user}
        
