from typing import Any, Text, Dict,Union, List ## Datatypes

from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import re

# class ActionSearch(Action):

#     def name(self) -> Text:
#         return "action_search"

#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         #Calling the DB
#         #calling an API
#         # do anything
#         #all caluculations are done
#         camera = tracker.get_slot('camera')
#         ram = tracker.get_slot('RAM')
#         battery = tracker.get_slot('battery')

#         dispatcher.utter_message(text='Here are your search results')
#         dispatcher.utter_message(text='The features you entered: ' + str(camera) + ", " + str(ram) + ", " + str(battery))
#         return []
########################

# class ActionShowLatestNews(Action):

#     def name(self) -> Text:
#         return "action_show_latest_news"

#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         #Calling the DB
#         #calling an API
#         # do anything
#         #all caluculations are done
#         dispatcher.utter_message(text='Here the latest news for your category')


#         return []

class User_details_form(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "user_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["name","number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        print("inside slot_mappings")
        
        return {"name":[self.from_text()],
                "number":[self.from_text()]
        }

    

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"))