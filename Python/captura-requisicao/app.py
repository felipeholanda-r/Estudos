from fastapi import FastAPI, Request

app = FastAPI()

# Interpreta requisições do tipo POST
@app.post("/{path:path}")
async def show_request_details(request: Request, path: str):

    client_host = request.client.host
    http_method = request.method
    url = request.url
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    client_data = await request.body()

    response = {
        "Client Host": client_host,
        "HTTP Method": http_method,
        "URL": url,
        "Headers": headers,
        "Query Parameters": query_params,
        "Request Body": client_data.decode() if client_data else None
    }
    print(response)
    return response

# Interpreta requisições do tipo GET
@app.get("/{path:path}")
async def show_request_details(request: Request, path: str):

    client_host = request.client.host
    http_method = request.method
    url = request.url
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    client_data = await request.body()

    response = {
        "Client Host": client_host,
        "HTTP Method": http_method,
        "URL": url,
        "Headers": headers,
        "Query Parameters": query_params,
        "Request Body": client_data.decode() if client_data else None
    }
    print(response)
    return response