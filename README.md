# Djangovents

Eventbrite functionality using Django.

Expected behaviour:

* Functional login page
* Logged in user can create new event
* Event's index page displays past and upcoming events
* Event's show page dispays list of attendants
* User's show page displays:
  - event's the user has created
  - event's the user has attended
  - event's the user will be attending
* Navigation links are present at the top of the page

Models:

* Event
* User
  - as event creator
  - as event attendee