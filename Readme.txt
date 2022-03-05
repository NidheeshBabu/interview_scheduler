DOCUMENTATION


Project Running Steps:
	Open folder 'test_entri' using any code editor/IDE/terminal
	install dependencies using pip: 'pip install -r requirements.txt'
	run local server: 'python manage.py runserver'
	API end point url for user registration: http://127.0.0.1:8000/scheduler/users   [POST]
			input data format: {
						"date": "05-03-2022",
        					"start_time": "11:20 AM",
        					"end_time": "01:20 PM",
        					"full_name": "Nidheesh Babu",
        					"role_name": "candidate"
						}
			(NB: role_name for interviewer is "interviewer", date and time must be in above format)
	API end point url for user listing: http://127.0.0.1:8000/scheduler/users    [GET]
	API end point url for slot calculating: http://127.0.0.1:8000/scheduler/time_slots?candidate_id=3&interviewer_id=5
			(NB: candidate_id and interviewer_id must be passed as query params)
	

Extra questions:

1. Better Solution: Interviewer can add Some available time slots for some particular days which should be saved in database. These time slots can be given to candidates so that they can 
			  choose an Suitable one. When a candidate confirms one of the time slot, that time slot should be removed from database. If the candidate is not available for all these
			  time slots then they can opt for another day, when the interviewer adds slots for next upcomming days that candidate can be included.

2. Improving existing solution: Both interviewer and candiate can add multiple time gaps that they will be available and slots can be choosen using that.


