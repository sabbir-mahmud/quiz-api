# quiz api server side:

## technology:
* Python
* Django (framework) 
* Django Rest Framework (framework)
* SimpleJWT (library)

## api details:
* https://sabbirquizapi.herokuapp.com/users-register/
with this api user can register themselves and get a account in the system.

* https://sabbirquizapi.herokuapp.com/api/login/
with this api user can login and get a token.

* https://sabbirquizapi.herokuapp.com/users/user-api/
with this api admin user can get all users in the system. this api is protected by token. only admin user can access this api.

* https://sabbirquizapi.herokuapp.com/quiz_api/
with this api user can see all the different quiz in the system. api is protected by token.

* https://sabbirquizapi.herokuapp.com/quiz_api/id/

https://sabbirquizapi.herokuapp.com/quiz_api/1/ with this api user can find a quiz by id.

* https://sabbirquizapi.herokuapp.com/quiz_api/id/id/
https://sabbirquizapi.herokuapp.com/quiz_api/1/1/ with this api user can find a single quiz question by id.

 