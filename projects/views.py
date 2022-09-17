from django.shortcuts import render
from projects.models import Image, Project

from django.core.paginator import Paginator

# Create your views here.
def projects(request):
	projects_list = Project.objects.all().order_by('-id')

	paginator = Paginator(projects_list, 1)
	page = request.GET.get('page', 1)
	try:
		projects = paginator.page(page)
	except PageNotAnInterger:
		projects = paginator.page(1)
	except EmptyPage:
		projects = paginator.page(paginator.num_pages)

	images = Image.objects.all()

	return render(request, 'projects.html', {
		'projects': projects,
		'images': images
	})