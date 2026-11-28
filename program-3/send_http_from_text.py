from pathlib import Path
import httpx

############################################

def restructure_text_file(text_file_path):

    with open(text_file_path, "r", encoding="utf-8") as text:
        text_file = text.read()
    
    split_text_lines = text_file.split("\n")
    req_first_line = split_text_lines[0].split(" ")
    
    req_method = req_first_line[0]
    req_uri = req_first_line[1]
    
    structured_output = []
    structured_output.append(f'{req_method}--{req_uri}')

    start_point = 1
    while start_point < len(split_text_lines):
        if len(split_text_lines[start_point]) == 0:
            start_point += 1
            continue

        if "{" in split_text_lines[start_point]:
            structured_output.append(split_text_lines[start_point])
            start_point += 1
            continue
    
        header_data = split_text_lines[start_point].split(":")
        header = header_data[0]
        payload = (",").join(header_data[1:])
    
        if header == "Referer":
            final_payload = payload.replace(",",":")
            structured_output.append(f'{header}--{final_payload}')
            start_point += 1
            continue
    
        structured_output.append(f'{header}--{payload}')
        start_point += 1

    return structured_output

############################################

def send_http_req(req_content_list):

    request_uri_data = req_content_list[0].split("--")

    request_method = request_uri_data[0]
    request_host = "".join(req_content_list[1].split("--")[1].split())
    request_uri = request_uri_data[1]

    request_uri_path = []
    request_headers = {}

    payload_method_list = ["POST","PATCH","PUT"]
    normal_method_list = ["GET","DELETE"]

######
    if request_method in normal_method_list:
        request_headers_list = req_content_list[1:]

        for single_header in request_headers_list:
            formated_header = single_header.split("--")
            request_headers[formated_header[0]] = "".join(formated_header[1].split())

        if "?" in request_uri:
            request_uri_params = {}

            request_uri_path.append(request_uri.split("?")[0])
            uri_params_list = request_uri.split("?")[1].split("&")

            request_url = f'https://{request_host}{request_uri_path[0]}'

            for single_param in uri_params_list:
                formated_param = single_param.split("=")
                request_uri_params[formated_param[0]] = formated_param[1]

            if request_method == 'GET':
                response = httpx.get(request_url, headers=request_headers, params=request_uri_params)
                return response.json()

            if request_method == 'DELETE':
                response = httpx.delete(request_url, headers=request_headers, params=request_uri_params)
                return response

        request_uri_path.append(request_uri)
        request_url = f'https://{request_host}{request_uri_path[0]}'

        if request_method == 'GET':
            response = httpx.get(request_url, headers=request_headers)
            return response.json()

        if request_method == 'DELETE':
            response = httpx.delete(request_url, headers=request_headers)
            return response

######
    if request_method in payload_method_list:
        request_headers_list = req_content_list[1:len(req_content_list)-1]

        request_payload = req_content_list[len(req_content_list)-1]
        request_uri_path.append(request_uri)

        request_url = f'https://{request_host}{request_uri_path[0]}'

        for single_header in request_headers_list:
            formated_header = single_header.split("--")
            request_headers[formated_header[0]] = "".join(formated_header[1].split())

        if request_method == 'POST':
            response = httpx.post(request_url, headers=request_headers, data=request_payload)
            return response.json()

        if request_method == 'PUT':
            response = httpx.put(request_url, headers=request_headers, data=request_payload)
            return response

        if request_method == 'PATCH':
            response = httpx.patch(request_url, headers=request_headers, data=request_payload)
            return response

############################################


with open("local_path_to_req.txt", "r", encoding="utf-8") as text:
    text_file = text.read()

input_text_file_path = Path("".join(text_file.split()))

data = restructure_text_file(input_text_file_path)
response = send_http_req(data)
print(response)




