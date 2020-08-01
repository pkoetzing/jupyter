import requests 
def get_json_response( url): 
    try: 
        r = requests.get( url) 
        return r.json() 
    except Exception as err: 
        print(err)
        raise err
get_json_response('test')