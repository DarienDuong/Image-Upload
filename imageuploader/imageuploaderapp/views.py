from django.shortcuts import render, redirect
from imageuploaderapp.forms import TopicForm, ImageForm

# Create your views here.
def home(request):
	topic_form = TopicForm()

	if request.method == "POST":
		topic_form = TopicForm(request.POST)
		if topic_form.is_valid():
			new_topic = topic_form.save(commit=False)
			new_topic.save()
			return redirect(home)

	return render(request, 'home.html', {"topic_form": topic_form})

def images(request):
	image_form = ImageForm()

	if request.method == "POST":
		image_form = ImageForm(request.POST, request.FILES)
	return render(request, 'image.html', {"image_form": image_form})
