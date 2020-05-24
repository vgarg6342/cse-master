# cse
sorry for the name now no going back


please install all the dependencies.
(pip install -r /path/to/requirements.txt -f file:///path/to/archive/)
REMEMBER USE VIRTUALENV
and put the project inside a directory inside the env dir.



i hope Django admin app is familiar to you create your own superuser and delete the exisitng sqlLite db(it can cause some problems)
please go though PHOTOLOGUE lib once for better understanding of the gallery model. No need to go into setup i already did that.

i guess 'Event' model is simple enough to understand with two gallery one for thumbnail photos and other for event coordinator photos with captions as their name

TODO

2. create a dashboard for the already logged in users(and sign up for the new one using Oauth)
3. model for workshop i.e extra features to add or deduct from the event model.
4. front end(bootstratp and jquery CDN is included in the base.html)
5. publication to AWS cloude as they provide 12 months free.

STRUCTURE

/events will give you list of all the events that hve been added

/events/(event_name)/ will give you all the details of the event added
  
