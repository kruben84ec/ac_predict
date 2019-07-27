from flask import Flask, jsonify, request, json, render_template

class Api():
	"""docstring for Api"""
	def __init__(self):
		"""Inicializa el servidor"""
		self.run_server = Flask(__name__)

	def responseApi(self, result):
		return jsonify(result)

