# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Use with data from https://earthquake.usgs.gov/earthquakes

import os
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import time

class Plot1(object):

	def __init__(self):
		self.mtitle = ''
		self.filename = ''
		self.data = ''
		self.all_eq_data = ''


	def load_data(self, filename):
		self.filename = filename	
		with open(self.filename) as f:
			self.all_eq_data = json.load(f)
		
	def parse_data(self):

		all_eq_dicts = self.all_eq_data['features']
		self.mtitle = self.all_eq_data['metadata']['title']
		mags, lons, lats, hover_texts = [], [], [], []
		for eq_dict in all_eq_dicts:
			mags.append( eq_dict['properties']['mag'])
			lons.append(eq_dict['geometry']['coordinates'][0])
			lats.append(eq_dict['geometry']['coordinates'][1])
			title = eq_dict['properties']['title']

			hover_texts.append(title)

		# Map the earthquakes.
		self.data = [{
			'type': 'scattergeo',
			'lon': lons,
			'lat': lats,
			'text': hover_texts,
			'marker': {
				'size': [5*mag for mag in mags],
				'symbol' : 'square',
				'color': 'crimson',
				'colorscale': 'Viridis',
				'reversescale': True,
				'colorbar': {'title': 'Magnitude'},
			},
		}]

	def do_plot(self):

		fig = { 'data': self.data }

		offline.plot(fig,image_filename=self.mtitle, image='png', auto_open=True, image_width=1000, image_height=500)
		time.sleep(2)
	

if __name__ == "__main__":

	p1 = Plot1() 
	p1.load_data('data/eq_data_1_day_m1.json')
	p1.parse_data()
	p1.do_plot()

	p7 = Plot1() 
	p7.load_data('data/eq_data_7_day_m1.json')
	p7.parse_data()
	p7.do_plot()

	p30 = Plot1() 
	p30.load_data('data/eq_data_30_day_m1.json')
	p30.parse_data()
	p30.do_plot()
