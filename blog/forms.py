from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	"""This is a for creating automated forms"""
	class Meta:
		model = Post
		fields = ('title', 'text',)







	