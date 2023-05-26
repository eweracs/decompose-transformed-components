# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class DecomposeTransformedComponents(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			"en": "Decompose Transformed Components",
			"de": "Transformierte Komponenten in Pfade umwandeln",
			"es": "Descomponer componentes transformados",
			"fr": "Supprimer les composants imbriqués",
			"ja": "変形したコンポーネントを分解",
			"ko": "변형된 컴포넌트 분해",
			"zh": "分解变形组件"
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		if not layer.components:
			return
		for component in layer.components:
			if component.transform != (1, 0, 0, 1, 0, 0):
				layer.decomposeComponents()
				break

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
