from django import forms

from imageuploaderapp.models import Topics, Images

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topics
		fields = ("name", "topic_id")

class ImageForm(forms.ModelForm):
	class Meta:
		model = Images
		fields = ("name", "image")