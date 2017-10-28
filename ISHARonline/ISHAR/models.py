from django.db import models
from django.utils.dateparse import parse_datetime


class Category(models.Model):
	category_name = models.CharField(max_length=255)

	def __str__(self):
		return self.category_name

class SubCategory(models.Model):
	category_name = models.CharField(max_length=255)
	parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.category_name


class Article(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	item_type = models.CharField(max_length=255, null=True)
	pub_year = models.CharField(max_length=255, null=True)
	author = models.CharField(max_length=255, null=True)
	title = models.CharField(max_length=255, null=True)
	pub_title = models.CharField(max_length=255, null=True)
	issn = models.CharField(max_length=255, null=True)
	doi = models.CharField(max_length=255, null=True)
	url = models.CharField(max_length=255, null=True)
	abstract = models.TextField(null=True)
	date = models.CharField(max_length=255, null=True)
	date_add = models.CharField(max_length=255, null=True)
	date_mod = models.CharField(max_length=255, null=True)
	date_access = models.CharField(max_length=255, null=True)
	pages = models.CharField(max_length=255,null=True)
	issue = models.CharField(max_length=255, null=True)
	volume = models.CharField(max_length=255,null=True)
	journal_abbr = models.TextField(null=True)
	short_title = models.TextField(null=True)
	language = models.CharField(max_length=255, null=True)
	lib_cat = models.CharField(max_length=255, null=True)
	url_link = models.CharField(max_length=255, null=True)
	extra = models.CharField(null=True, max_length=255)
	tags = models.TextField(max_length=255, null=True)

	def __str__(self):
		return self.pub_title

	def short_abstract(self):
		try:
			short = self.abstract.split (".", 10)[9] + "..."
			if (len(short) < 50):
				return self.abstract
			else:
				return short
		except:
			return self.abstract

	def format_tags(self):
		return self.tags.split(';')

	def to_lang(self):
		return {
			'eng': "English",
			'fre': "French",
			'hun': "Hungarian",
			'jpn': "Japanese",
			'ger': "German",
			'nor': "Norweigan",
			'spa': "Spanish",
			'kor': "Korean",
			'ita': "Italian"
		}.get(self.language.lower(), "English")
	
class Journal(models.Model):
	journal_name = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	summary = models.CharField(max_length=255)

	def __str__(self):
		return self.journal_name