import requests
import json

class BRIDGE(object):
    """
    docstring
    """
    def __init__(self):
        """
        Section initalizes bridge, I will need to create method for when button presses are required
        on the bridge, thats a later problem
        """
        self.ip=get_ip()
    
def get_ip():
    """
    This method should be updated according to:
        https://developers.meethue.com/develop/application-design-guidance/hue-bridge-discovery/
        to follow the different types of querying, this is the easiest way to get i
    """
    query= requests.get('https://discovery.meethue.com')
    bridge_return = json.loads(query.text)
    return bridge_return[0]['internalipaddress']
