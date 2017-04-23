
from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------
level_list = {
    "1" : {"hi", "you", "we" },
    "2" : {"butter", "beans", "chunks"},
    "3" : {"busy", "greatest", "fishing"}
}

data = {}

five_set = ["busy", "grips", "flipper", "please", "flower"]
counter = 0
score = 0

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + str(title),
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    card_title = "Welcome"
    session_attributes = {}
    should_end_session = False
    speech_output = "Welcome to Kepeesh, the spelling application for kids, " \
    "Let me know when you're ready to start by saying, start" 
    reprompt_text = "Let me know when you're ready to start by saying, start" 
    return build_response({}, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_started_response(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    global data
    card_title = "Start"
    should_end_session = False
    data['Level'] = -1
    data['Score'] = 0

    speech_output = "Please tell me the grade level spelling you want to start at by saying Level then a number from 1 to 3" 
    reprompt_text = "Please tell me the grade level spelling you want to start at by saying Level then a number from 1 to 3"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def create_level_attributes(current_level):
    return {"currentLevel": current_level}

def handle_level_response(intent, session): 
    global data
    card_title = intent['name']
    should_end_session = False
    #session['attributes'] = {}
    current_level = intent['slots']['Level']
    nums = ["1", "2", "3"]
    if current_level['value'] in nums: 
        level = current_level['value']
        data['Level'] = level
        speech_output = "You are now on level " + level + " Are you ready to start spelling? Answer Yes to start, Change to change level, or No to quit"
        reprompt_text = "Are you ready to start spelling?" 
        card_title = level
    else:
        #session_attributes = create_level_attributes(current_level)
        speech_output = "That level is not represented. Please choose a level from 1 to 3."
        reprompt_text = "Try another level from 1 to 3"
        card_title = "Invalid Level"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handler_change_response(intent, session):
    card_title = "Change"
    speech_output = "What level do you want to change to? Say Level followed by a number from 1 to 3"
    reprompt_text = speech_output
    should_end_session = False

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



#def each_word_output()
def handler_yes_response(intent, session):
    global counter, data
    card_title = "Yes"
    word = five_set[counter]

    speech_output = "Now spell, " + word
    reprompt_text = speech_output
    should_end_session = False

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_letters_response(word_list, intent, session):
    global counter, score, data
    card_title = "Letters"
    should_end_session = False
    word = word_list[counter]
    user_guess = intent['slots']['Letter']['value'] 
    concat_guess = user_guess.replace(" ", "")
    counter += 1
    if counter == 5:
        counter = 0

    if word.lower() == concat_guess.lower():
        score += 1
        speech_output = "Correct, " + word + " is spelled, " + user_guess + ". Now for your next word," + word_list[counter]
        reprompt_text = speech_output

    else:
        speech_output = "Wrong, " + word + " is spelled, " + word.replace(""," ") + " . Now for your next word, " \
        + word_list[counter]  #+ " " + str(len(word)) + " vs. " + str(len(concat_guess))
        score -= 1
        reprompt_text = speech_output

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handler_score_response(intent, session):
    global score
    card_title = "score"
    speech_output = "You currently have " + str(score) + " points!"
    reprompt_text = speech_output
    should_end_session = False

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_help_response(intent, session):
    global data
    if not data['Level'] == -1 :
        speech_output = "You haven't set a level yet." + " Say a level from 1-3"
        reprompt_text = speech_output
    else:
        speech_output = "You are on level " + str(data['Level'])
        reprompt_text = speech_output
    should_end_session = False
    card_title = "Help Response"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for spelling today. It was easy, Kepeesh! " \
    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
    + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
    ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
    ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']   #get intent, and name from intent_request
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers/funcs
    if intent_name == "LevelStart":
        return get_started_response(intent, session)
    elif intent_name == "SetLevel":
        return handle_level_response(intent, session)
    elif intent_name == "Letters":
        word_list = five_set
        return handle_letters_response(word_list, intent, session)
    elif intent_name == "ScoreCheck":
        return handler_score_response(intent, session)
    elif intent_name == "ChangeIntent":
        return handler_change_response(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return handler_yes_response(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_response(intent, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
    ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
    event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
        event['session'])

    if event['request']['type'] == "LaunchRequest":     # if request is a LaunchRequest, start the skill
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":   # if request is an IntentRequest, check what type of intent it is 
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest": #if request is an EndRequest, end the skill
        return on_session_ended(event['request'], event['session'])


