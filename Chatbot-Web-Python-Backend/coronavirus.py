import requests
import json
import re
import threading
import time
from spellchecker import SpellChecker

API_KEY = "tQUqTjHrbqM-"
PROJECT_TOKEN = "tfs3cuE3x4Cf"

class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.data = self.get_data()

	def get_data(self):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		data = json.loads(response.text)
		
		return data

	def get_total_cases(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Coronavirus Cases:":
				return "Total Coronavirus <b>Cases</b> in the <b>World : " + content['value'] + "</b>"

	def get_total_deaths(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Deaths:":
				return "Total Coronavirus <b>Deaths</b> in the <b>World : " + content['value'] + "</b>"

		return "0"

	def get_total_cases_recovered(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Recovered:":
				return "Total Coronavirus <b>Recovered</b> Cases in the <b>World : " + content['value'] + "</b>"



	def get_country_data(self, country):
		data = self.data["country"]

		for content in data:
			if content['name'].lower() == country.lower():
				return content

		return "0"

	def get_list_of_countries(self):
		countries = []
		for country in self.data['country']:
			countries.append(country['name'].lower())

		return countries

	def update_data(self):
		response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)


def coronavirus_data(text):
	
	data = Data(API_KEY, PROJECT_TOKEN)

	country_list = data.get_list_of_countries()

	TOTAL_PATTERNS = {

	                # Recovered
					re.compile("[\w\s]+total [\w\s]+ recovered [\w\s]+"):data.get_total_cases_recovered,
					re.compile("[\w\s]+ recovered [\w\s]+"):data.get_total_cases_recovered,

					# Total cases
					re.compile("[\w\s]+total[\w\s]+cases[\w\s]+"):data.get_total_cases,
					re.compile("total [\w\s]+ cases"): data.get_total_cases,

                    re.compile("[\w\s]+total[\w\s]+deaths[\w\s]+"): data.get_total_deaths,
                    re.compile("total [\w\s]+ deaths"): data.get_total_deaths,

					re.compile("[\w\s]+total[\w\s]+case[\w\s]+"):data.get_total_cases,
					re.compile("total [\w\s]+ case"): data.get_total_cases,
                    re.compile("[\w\s]+total[\w\s]+death[\w\s]+"): data.get_total_deaths,
                    re.compile("total [\w\s]+ death"): data.get_total_deaths,

                    # Without total

					re.compile("[\w\s]+cases[\w\s]+"):data.get_total_cases,
					re.compile("total [\w\s]+ cases"): data.get_total_cases,

                    re.compile("[\w\s]+deaths[\w\s]+"): data.get_total_deaths,
                    re.compile("[\w\s]+ deaths"): data.get_total_deaths,

					re.compile("[\w\s]+case[\w\s]+"):data.get_total_cases,
					re.compile("[\w\s]+ case"): data.get_total_cases,
                    re.compile("[\w\s]+death[\w\s]+"): data.get_total_deaths,
                    re.compile("[\w\s]+ death"): data.get_total_deaths,

					}

	COUNTRY_PATTERNS = {
					re.compile("[\w\s]+ cases [\w\s]+"): lambda country: "Coronavirus <b>Cases</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['total_cases'] + "</b>",
					re.compile("[\w\s]+ case [\w\s]+"): lambda country: "Coronavirus <b>Cases</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['total_cases'] + "</b>",

                    re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: "Coronavirus <b>Deaths</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['total_deaths'] + "</b>",
                    re.compile("[\w\s]+ death [\w\s]+"): lambda country: "Coronavirus <b>Deaths</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['total_deaths'] + "</b>",
					
					re.compile("[\w\s]+ new cases [\w\s]+"): lambda country: "Coronavirus <b>New Cases</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['new_cases'] + "</b>",
					re.compile("[\w\s]+ new case [\w\s]+"): lambda country: "Coronavirus <b>New Cases</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['new_cases'] + "</b>",

                    re.compile("[\w\s]+ new deaths [\w\s]+"): lambda country: "Coronavirus <b>New Deaths</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['new_deaths'] + "</b>",
                    re.compile("[\w\s]+ new death [\w\s]+"): lambda country: "Coronavirus <b>New Deaths</b> in <b>" + country.capitalize() + " : " + data.get_country_data(country)['new_deaths'] + "</b>",
					
                    # Recovered

					re.compile("[\w\s]+ recovered [\w\s]+"): lambda country: "Coronavirus <b>Recovered Cases</b> in " + country.capitalize() + " : " + data.get_country_data(country)['total_recovered'] + "</b>",

					re.compile("[\w\s]+ total recovered [\w\s]+"): lambda country: "Coronavirus <b>Recovered Cases</b> in " + country.capitalize() + " : " + data.get_country_data(country)['total_recovered'] + "</b>",

					}


	result = None

	for pattern, func in TOTAL_PATTERNS.items():
		if pattern.match(text):
			result = func()
			break

	for pattern, func in COUNTRY_PATTERNS.items():
		if pattern.match(text):
			words = set(text.split(" "))
			for country in country_list:
				if country in words:
					result = func(country)
					break


	if result == None:

		if "coronavirus" in text.lower() or "covid" in text.lower() or "covid19" in text.lower() or "cor" and "virus" in text.lower():   
			result = "I can give you the coronavirus updates!<br>Type one of the following :<br><br><div style='font-size: small;'><i class='fa fa-info-circle blue'></i> Covid19 [cases/deaths/recovered] in the World<br><i class='fa fa-info-circle blue'></i> Covid19 (new)[cases/deaths/recovered] in [Country]</div>"

	return result


