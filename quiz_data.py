import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]


"""
Sample Response

[
    {
        'category': 'Sports', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'Which Footballer is also known as Sniper?',
        'correct_answer': 'Toni Kroos', 
        'incorrect_answers': [
            'Luka Modric', 
            'Federico Valverde', 
            'Thomas Müller'
            ]
    }, 
    {
        'category': 'Entertainment: Music', 
        'type': 'multiple', 
        'difficulty': 'medium', 
        'question': 'In which city did American rap producer DJ Khaled originate from?',
        'correct_answer': 'Miami', 
        'incorrect_answers': [
            'New York', 
            'Detroit', 
            'Atlanta'
            ]
        }
]
"""