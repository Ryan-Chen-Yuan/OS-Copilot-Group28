from oscopilot import FridayAgent
from oscopilot import ToolManager
from oscopilot import FridayExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run
import base64
import requests

# OCR_ACCESS_KEY Baidu OCR API's key
# Note that this is a temporary key and needs to be replaced if expires.
OCR_ACCESS_KEY = (
    "24.d92099366a06a098f27f7914a6c7344e.2592000.1734953066.282335-116368149"
)


def ocr(image_path):
    """
    Generates a dictionary of words and their respective coordinates in the image and an encoded image for API requests.

    Args:
        image_path (str): path to the image file

    Returns:
        dict: dictionary of words and their respective coordinates in the image
        str: encoded image for API requests
    """
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    f = open(image_path, "rb")
    img = base64.b64encode(f.read())
    params = {"image": img, "paragraph": "false", "probability": "false"}
    access_token = OCR_ACCESS_KEY
    request_url = request_url + "?access_token=" + access_token
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if response.json()["words_result"]:
            dict = {}
            for item in response.json()["words_result"]:
                dict[item["words"]] = (
                    item["location"]["left"] + item["location"]["width"] // 2,
                    item["location"]["top"] + item["location"]["height"] // 2,
                )
            return (dict, img.decode("utf-8"))
        else:
            raise Exception("No words found in the image")
    else:
        raise Exception("OCR failed")


template = """
Please use AppleScript or Python to help me complete some automation operations in Mac. 
I will send you the corresponding text or pictures and tell you the detailed requirements. 
According to the following information: '{event_text}', 
follow the steps below: 
1. use Python to parse string to datetime objects; 
2. use Python to format datetime objects; 
3. Use AppleScript to add calendar event with the time formatted in the step2(format datetime objects) and other information into 'Personal' calendar.
note: create calendar 'Personal' if absent.
"""

args = setup_config()
if not args.query:
    event_text = "Dec 11 WED 6:30 pm - 8:30 pm COMP7107 Management of complex data types Venue: CPD-LG.07-10, Centennial Campus"
else:
    event_text = args.query
if args.query_file_path:
    img_path = args.query_file_path
    label_dict, _ = ocr(img_path)
    event_text = " ".join(label_dict.keys())
args.query = template.format(event_text=event_text)
task = setup_pre_run(args)
agent = FridayAgent(
    FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args
)
agent.run(task=task)
