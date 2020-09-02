from typing import Any, Text, Dict, List

from Database import Database
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# TODO: store activity in database
# TODO: get activity duration and date

class ActionProcessActivity(Action):

    def name(self) -> Text:
        return "action_process_activity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        db = Database()
        db.connect()

        activity = tracker.get_slot('activity')

        if activity:
            db.insertActivity(activity, 30)
            dispatcher.utter_message(f"Keep {activity}!")
        else:
            print('No activity!')

        return []
