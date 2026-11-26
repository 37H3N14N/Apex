import os
import json
import base64
import re
from pathlib import Path

###########################################################################

def group_traffic_from_json_file(file_name,arg_write,arg_uri,arg_host):

    with open(f'apex/json-files/{file_name}', encoding= 'utf-8') as file:
        json_data = json.load(file)


    synopsis_data = {}
    write_data = {}

    for entity in json_data:

        host_name = entity['host']
        request_method = entity['method']
        request_path = entity['path']
        request_length = entity['length']

        if arg_host[0] == 'hosts':

            if host_name in arg_host[1]:
                
                if arg_uri[0] == 'specific_uri':
                    uri_component_list = arg_uri[1].split("/")
                    request_path_component_list = request_path.split("/")

                    if all(item in request_path_component_list for item in uri_component_list):

                        if arg_write == 'synopsis':

                            if synopsis_data.get(host_name):
                                custom_uri = f'{request_path}__{request_method}'
                                existing_uri_list = synopsis_data[host_name]

                                if custom_uri not in existing_uri_list:
                                    synopsis_data[host_name].append(f'{request_path}__{request_method}')

                            if not synopsis_data.get(host_name):
                                synopsis_data[host_name] = [f'{request_path}__{request_method}']

                        if arg_write == 'write_files':
                            custom_uri = f'{request_path}__{request_method}'
                            http_pair = []

                            try:
                                if entity['raw']:
                                    decode_raw_request = base64.b64decode(entity['raw'])
                                    readable_raw_request = decode_raw_request.decode('utf-8')
                                    http_pair.append(readable_raw_request)

                                    decode_raw_response = base64.b64decode(entity['response']['raw'])
                                    readable_raw_response = decode_raw_response.decode('utf-8') 
                                    http_pair.append(readable_raw_response)
                            except:
                                continue

                            if write_data.get(custom_uri):
                                existing_uri_list = write_data[custom_uri]
                                write_data[f'{custom_uri}---{[len(existing_uri_list)]}'] = {
                                    "request":http_pair[0],
                                    "response":http_pair[1]
                                }

                            if not write_data.get(custom_uri):
                                write_data[custom_uri] = {
                                    "request":http_pair[0],
                                    "response":http_pair[1]
                                }


                if arg_uri[0] == 'wildcard':

                    if arg_write == 'synopsis':

                        if synopsis_data.get(host_name):
                            custom_uri = f'{request_path}__{request_method}'
                            existing_uri_list = synopsis_data[host_name]

                            if custom_uri not in existing_uri_list:
                                synopsis_data[host_name].append(f'{request_path}__{request_method}')

                        if not synopsis_data.get(host_name):
                            synopsis_data[host_name] = [f'{request_path}__{request_method}']


                    if arg_write == 'write_files':
                        custom_uri = f'{request_path}__{request_method}'
                        http_pair = []

                        try:
                            if entity['raw']:
                                decode_raw_request = base64.b64decode(entity['raw'])
                                readable_raw_request = decode_raw_request.decode('utf-8')
                                http_pair.append(readable_raw_request)

                                decode_raw_response = base64.b64decode(entity['response']['raw'])
                                readable_raw_response = decode_raw_response.decode('utf-8') 
                                http_pair.append(readable_raw_response)
                        except:
                            continue

                        if write_data.get(custom_uri):
                            existing_uri_list = write_data[custom_uri]
                            write_data[f'{custom_uri}---{[len(existing_uri_list)]}'] = {
                                "request":http_pair[0],
                                "response":http_pair[1]
                            }

                        if not write_data.get(custom_uri):
                            write_data[custom_uri] = {
                                "request":http_pair[0],
                                "response":http_pair[1]
                            }
                


        if arg_host[0] == 'all':

            if arg_uri[0] == 'specific_uri':
                uri_component_list = arg_uri[1].split("/")
                request_path_component_list = request_path.split("/")

                if all(item in request_path_component_list for item in uri_component_list):

                    if arg_write == 'synopsis':

                        if synopsis_data.get(host_name):
                            custom_uri = f'{request_path}__{request_method}'
                            existing_uri_list = synopsis_data[host_name]

                            if custom_uri not in existing_uri_list:
                                synopsis_data[host_name].append(f'{request_path}__{request_method}')

                        if not synopsis_data.get(host_name):
                            synopsis_data[host_name] = [f'{request_path}__{request_method}']


                    if arg_write == 'write_files':
                        custom_uri = f'{request_path}__{request_method}'
                        http_pair = []

                        try:
                            if entity['raw']:
                                decode_raw_request = base64.b64decode(entity['raw'])
                                readable_raw_request = decode_raw_request.decode('utf-8')
                                http_pair.append(readable_raw_request)

                                decode_raw_response = base64.b64decode(entity['response']['raw'])
                                readable_raw_response = decode_raw_response.decode('utf-8') 
                                http_pair.append(readable_raw_response)
                        except:
                            continue

                        if write_data.get(custom_uri):
                            existing_uri_list = write_data[custom_uri]
                            write_data[f'{custom_uri}---{[len(existing_uri_list)]}'] = {
                                "request":http_pair[0],
                                "response":http_pair[1]
                            }

                        if not write_data.get(custom_uri):
                            write_data[custom_uri] = {
                                "request":http_pair[0],
                                "response":http_pair[1]
                            }


            if arg_uri[0] == 'wildcard':

                    if arg_write == 'synopsis':

                        if synopsis_data.get(host_name):
                            custom_uri = f'{request_path}__{request_method}'
                            existing_uri_list = synopsis_data[host_name]

                            if custom_uri not in existing_uri_list:
                                synopsis_data[host_name].append(f'{request_path}__{request_method}')

                        if not synopsis_data.get(host_name):
                            synopsis_data[host_name] = [f'{request_path}__{request_method}']


                    if arg_write == 'write_files':
                        custom_uri = f'{request_path}__{request_method}'
                        http_pair = []

                        try:
                            if entity['raw']:
                                decode_raw_request = base64.b64decode(entity['raw'])
                                readable_raw_request = decode_raw_request.decode('utf-8')
                                http_pair.append(readable_raw_request)

                                decode_raw_response = base64.b64decode(entity['response']['raw'])
                                readable_raw_response = decode_raw_response.decode('utf-8') 
                                http_pair.append(readable_raw_response)
                        except:
                            continue

                        if write_data.get(custom_uri):
                            existing_uri_list = write_data[custom_uri]
                            write_data[f'{custom_uri}---{[len(existing_uri_list)]}'] = {
                                "request":http_pair[0],
                                "response":http_pair[1]
                            }

                        if not write_data.get(custom_uri):
                            write_data[custom_uri] = {
                                "request":http_pair[0],
                                "response":http_pair[1]
                            }

    return [synopsis_data,write_data]

###########################################################################

def organised_results_output(data_list,folder_destination):

    if len(data_list[0]) > 0 :

        print('----------- [ SYNOPSIS ] ---------------')
        item_count = 1

        for key,value in data_list[0].items():
            print(f'[ ITEM_NO = {item_count} ] | [ HOST = {key} ] | [ URIs_NO = {len(value)} ]')
            for one_uri in value:
                print(f'[URI]: {one_uri}') 
            print('-----------------------------------')
            item_count += 1

    if len(data_list[1]) > 0 :

        print('----------- [ WRITING FILES ] ---------------')
        item_count = 1

        for key,value in data_list[1].items():

            key_replace_1 = key.replace("_","-")
            key_name = key_replace_1.replace("/","_")

            uri_subfolder_path = Path(f'{folder_destination}/[{key_name}]')
            uri_subfolder_path.mkdir(parents=True, exist_ok=True)

            req_file_path = uri_subfolder_path/'req.md'
            res_file_path = uri_subfolder_path/'res.md'

            with open(req_file_path , "w") as file:
                file.write(value['request'])

            with open(res_file_path , "w") as file:
                file.write(value['response'])


            print(f'File [{item_count}] written')
            item_count += 1

        

###########################################################################

with open('apex/program-2/search_config/search.json','r') as file:
    search_detail = json.load(file)

arg_folder_destination=search_detail['folder_destination_path']

result_list = group_traffic_from_json_file(
    file_name=search_detail['file_name'],
    arg_write =search_detail['synopsis_or_write_files'],
    arg_uri=search_detail['specific_uri_or_wildcard'],
    arg_host=search_detail['hosts_or_all'],
    )


organised_results_output(result_list,arg_folder_destination)


###########################################################################


