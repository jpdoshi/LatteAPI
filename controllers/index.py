from utils.responses import TextResponse
from utils.requests import Request

def controller():
	msg = "Hello, World!"
	return TextResponse(msg)