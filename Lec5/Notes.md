


## API Request Types

* requests.get(url) - GET: retrieve resource
* requests.post(url) - POST: create a new resource
* requests.put(url) - PUT: replace a resource
* requests.patch(url) - PATCH: update a resource
* requests.delete(url) - DELETE: delete a resource

Response codes:

* 200 - ok
* 291 - Created
* 400 - Bad request
* 403 - Forbidden
* 404 - Not found (also request doesn't exist)
* 405 - Method Not Allowed (eg: GET only method POST not allowed)
* 422 - Unprocessable Entity
