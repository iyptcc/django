from .models import Template

# each template type has a default context to test the template with

default_template_context={
    Template.REGISTRATION:
    [
            {
                "data": [
                    {
                        "list": [
                            "Changi (SIN)",
                            "City Airport"
                        ],
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": None
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "2018-07-01 06:00:00+00:00"
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "Small"
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": ""
                    },
                    {
                        "needed": True,
                        "optional": True,
                        "required": False,
                        "value": "3"
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "2018-02-28"
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "blubb"
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "male"
                    },
                    {
                        "needed": True,
                        "optional": True,
                        "required": False,
                        "value": ""
                    },
                    {
                        "needed": True,
                        "optional": True,
                        "required": False,
                        "value": "King II K."
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "2018-02-21 21:43:00+00:00"
                    },
                    {
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": "False"
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "image": {
                            "id": 179,
                            "url": "50jahreuulm_9EhYn3J.jpg"
                        },
                        "needed": True,
                        "optional": False,
                        "required": True,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    }
                ],
                "email": "fe-iyptcc-localhost-root@nlogn.org",
                "first_name": "Root",
                "last_name": "van Engelmann",
                "team": [
                    "Austria",
                    "Brazil",
                    "China",
                    "MyOrigin",
                    "Sweden",
                    "Taiwan",
                    "United Kingdom",
                    "Wien"
                ],
                "properties": [
                    "Pickup",
                    "Arrival Time",
                    "Single Choice",
                    "color",
                    "Ponies",
                    "Date of Birth",
                    "Remarks",
                    "Sex",
                    "Preferred Name",
                    "Preferred Name (short)",
                    "Departure Time",
                    "Attend IOC",
                    "Conflicting Origins",
                    "Passport",
                    "Nationality",
                    "AGB",
                    "CV",
                    "Upgrade Single room"
                ]
            },
            {
                "data": [
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    },
                    {
                        "needed": False,
                        "optional": False,
                        "required": False,
                        "value": None
                    }
                ],
                "email": "fe-cc-test1@nlogn.org",
                "first_name": "Felix One",
                "last_name": "Engelmann",
                "team": [
                    "Australia"
                ],
                "properties": [
                    "Pickup",
                    "Arrival Time",
                    "Single Choice",
                    "color",
                    "Ponies",
                    "Date of Birth",
                    "Remarks",
                    "Sex",
                    "Preferred Name",
                    "Preferred Name (short)",
                    "Departure Time",
                    "Attend IOC",
                    "Conflicting Origins",
                    "Passport",
                    "Nationality",
                    "AGB",
                    "CV",
                    "Upgrade Single room"
                ]
            }
        ]
}
