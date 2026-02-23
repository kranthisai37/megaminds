from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required
def dashboard(request):

    if request.user.role == 'admin':
        projects = Project.objects.all()

    elif request.user.role == 'lead':
        projects = Project.objects.filter(project_lead=request.user)

    else:
        projects = request.user.dev_projects.all()

    return render(request, 'dashboard.html', {'projects': projects})

#role based decorator
from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("You are not authorized to access this page.")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

#create Project

from .forms import ProjectForm
from django.shortcuts import redirect


@login_required
@role_required(['admin'])
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})

#Assign developers to projects
from core.forms import AssignDeveloperForm
@login_required
@role_required(['lead'])
def assign_developers(request, project_id):
    project = Project.objects.get(id=project_id)

    # Security check: Lead can only assign to their own project
    if project.project_lead != request.user:
        return HttpResponseForbidden("You cannot modify this project.")

    if request.method == 'POST':
        form = AssignDeveloperForm(request.POST)
        if form.is_valid():
            developers = form.cleaned_data['developers']
            project.developers.set(developers)
            return redirect('dashboard')
    else:
        form = AssignDeveloperForm(initial={
            'developers': project.developers.all()
        })

    return render(request, 'assign_developers.html', {
        'form': form,
        'project': project
    })

#document upload
from core.forms import DocumentForm
@login_required
@role_required(['admin', 'lead'])
def upload_document(request, project_id):
    project = Project.objects.get(id=project_id)

    # Security check: Lead can only upload to their own project
    if request.user.role == 'lead' and project.project_lead != request.user:
        return HttpResponseForbidden("You cannot upload to this project.")

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.project = project
            document.uploaded_by = request.user
            document.save()
            return redirect('dashboard')
    else:
        form = DocumentForm()

    return render(request, 'upload_document.html', {
        'form': form,
        'project': project
    })


#viewing documents

@login_required
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)

    # Admin can view all
    if request.user.role == 'admin':
        pass

    # Lead can view only their project
    elif request.user.role == 'lead' and project.project_lead != request.user:
        return HttpResponseForbidden("Not allowed.")

    # Developer must be assigned
    elif request.user.role == 'dev' and request.user not in project.developers.all():
        return HttpResponseForbidden("Not allowed.")

    documents = project.document_set.all()

    return render(request, 'project_detail.html', {
        'project': project,
        'documents': documents
    })