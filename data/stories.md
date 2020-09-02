## happy path
* greet
  - utter_greet
  - utter_ask_activity
* report_activity
  - action_process_activity
  - utter_encourage
* goodbye
  - utter_goodbye

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
