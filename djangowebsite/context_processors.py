def get_sections(request):
    sections = {('articles', 'main:articles'), ('about', 'main:homepage'), ('data', 'main:data')}
    print('yeet')
    return {'sections': sections}