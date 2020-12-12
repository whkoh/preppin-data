import pandas as pd
from pandas.io.json import json_normalize

qo = {
	"orders": [
		{
			"size": "medium",
			"price": 15.67,
			"toppings": ["mushrooms", "pepperoni", "basil"],
			"extra_cheese": False,
			"delivery": True,
			"client": {
				"name": "Jane Doe",
				"phone": '',
				"email": "janedoe@email.com"
			}
		},
		{
			"size": "small",
			"price": 6.54,
			"toppings": [],
			"extra_cheese": True,
			"delivery": False,
			"client": {
				"name": "Foo Jones",
				"phone": "556-342-452",
				"email": ""
			}
		}
	]
}

q = json_normalize(qo['orders'], sep='_')
r = json_normalize(qo['orders'], record_path=['toppings'])