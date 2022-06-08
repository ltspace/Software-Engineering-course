def index(request):
    text = IndexModel.objects.get(id=1)
    return render(request, 'index.html', {'text': text})