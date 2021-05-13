# Instructions to install and run the databases correctly:

- create "gala_chatbot" and "gala_feedback" blank databases in postgresql (code tested on pgAdmin4)
- Open terminal, type "python"
- type these instructions:
>>> from app import db
>>> db.create_all()
>>> exit()
- Open IDE, open chatbot.py.
- comment the big training list (lines 48-53)
- decomment the "greetings.yml" training line (line 45)
- run chatbot.py to create the database
- go to your database, alter table properties:
-- statement:length/precision of text,search_text,in_response_to,search_in_response_to to 1,000
-- statement:length/precision of conversation,persona to 100
-- tag: length/precision of name to 100
- decomment the big training list (lines 48-53)
- comment the greetings training line (line 45)
- run chatbot.py to finish the training
- comment both training lists 
- run/test program typing python app.py



