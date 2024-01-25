from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ValidateOrder(Action):

    def name(self) -> Text:
        return "validate_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = tracker.get_slot('food')
        drink = tracker.get_slot('drink')
        return [SlotSet("food", food), SlotSet("drink", drink)]

class CalculateTotal(Action):

    def name(self) -> Text:
        return "calculate_total"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prices = {'pizza': 12, 'burger': 8, 'lasagne': 6, 'eau': 2, 'café': 2, 'coca': 3}
        food = tracker.get_slot('food')
        drink = tracker.get_slot('drink')
        total_price = prices.get(food, 0) + prices.get(drink, 0)
        return [SlotSet("total_price", total_price)]
