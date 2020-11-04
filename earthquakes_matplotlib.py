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

class PlotEarthquake(object):

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
			},
		}]

	def do_plot(self):
		self.mlayout = Layout(title=self.mtitle)
		fig = { 'data': self.data, 'layout' : self.mlayout}
		offline.plot(fig, filename=self.mtitle+'.html', image_filename=self.mtitle, image='png', auto_open=True, image_width=1000, image_height=500)
		time.sleep(2)

if __name__ == "__main__":
	# make objects from files in 'data' dir - 1 graph per json file
	eq_json = ['data/eq_data_1_day_m1.json', 'data/eq_data_7_day_m1.json',  'data/eq_data_30_day_m1.json']
	for i in range (0,len(eq_json)):
		plotn = "p_"+str(i)
		plotn = PlotEarthquake()
		plotn.load_data(eq_json[i])
		plotn.parse_data()
		plotn.do_plot()
