import requests

class RequestsUtil:

    def send_request_nodata(self,method,url,**kwargs):
        rep = requests.request(method,url,**kwargs)
        return rep.text


    def send_request(self,method,url,data = None,**kwargs):
        rep = requests.request(method,url,data,**kwargs)
        return rep.text


