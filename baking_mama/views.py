from django.shortcuts import render

# This views file is accessible to the whole project, 
# rather than being part of the baking mama or recipes app.
# See documentation: https://docs.djangoproject.com/en/3.2/topics/http/views/#customizing-error-views


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)