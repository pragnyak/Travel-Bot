from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return HttpResponse('Hello World!')


@csrf_exempt
def webhook(request):
    # build a request object
	req = json.loads(request.body)

	# get action from json

	action = req.get('queryResult').get('action')
	
	if action == 'day':
		
		days=req.get('queryResult').get('queryText')
		fromday=req.get('queryResult').get('parameters').get("number1")
		
		today=req.get('queryResult').get('parameters').get("number")
		
		# return a fulfillment message
		#fulfillmentText = {'fulfillmentMessages':[ 'Great.Hope you are combining weekends to save on your leaves!!',['hello']]}

		if not today:
			fromday=fromday
		elif not fromday:
			fromday=today

		if today and fromday:
			if today<fromday:
				fromday,today=today,fromday


		if int(fromday)<3:
			reply={"fulfillmentMessages": [
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "'Thats a nice short little gateway!'"
		        }
		      ]
		    }
		  },
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "What would you like to do in this break?"
		        }
		      ]
		    }
		  },
		  {
		    "text": {
		      "text": [
		        ""
		      ]
		    }
		  }
		]}
		elif fromday<=5 or (fromday>=3 and today<=5):
			reply={"fulfillmentMessages": [
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "'Great.Hope you are combining weekends to save on your leaves!!'"
		        }
		      ]
		    }
		  },
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "What would you like to do in this break?"
		        }
		      ]
		    }
		  },
		  {
		    "text": {
		      "text": [
		        ""
		      ]
		    }
		  }
		]}
		else:
			reply={"fulfillmentMessages": [
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "'Yuhoo! I like that.Gives you a lot of time to soak up the place.'"
		        }
		      ]
		    }
		  },
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "What would you like to do in this break?"
		        }
		      ]
		    }
		  },
		  {
		    "text": {
		      "text": [
		        ""
		      ]
		    }
		  }
		]}



		# reply = {

		# "fulfillmentText": "Ok. Tickets booked successfully.",
		# # "fulfillmentMessage": ['Great.Hope you are combining weekends to save on your leaves!!','hello'],
		# }
		return JsonResponse(reply,safe=False)
	
	elif action == 'activity':
		text=req.get('queryResult').get('queryText')
		activitypara=req.get('queryResult').get('parameters')
		print(activitypara)
		reply1={"fulfillmentMessages": [
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "'Nice choices!I need a few more details before I can search and find your matching itinerary.'"
		        }
		      ]
		    }
		  },
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "Who are you travelling with?"
		        }
		      ]
		    }
		  },
		  {
		    "text": {
		      "text": [
		        ""
		      ]
		    }
		  }
		]}
		return JsonResponse(reply1,safe=False)

	elif action == "type":

		typepara=req.get('queryResult').get('parameters')
		print(typepara)
		reply2={"fulfillmentMessages": [
		  {
		    "platform": "ACTIONS_ON_GOOGLE",
		    "simpleResponses": {
		      "simpleResponses": [
		        {
		          "textToSpeech": "'Awesome ,I have all the required details.Kindly give me some time while I scan my itineraries and find you a match:)'"
		        }
		      ]
		    }
		  },
		  
		  {
		    "text": {
		      "text": [
		        ""
		      ]
		    }
		  }
		]}
		return JsonResponse(reply2,safe=False)

	






		