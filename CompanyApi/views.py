from django.http import HttpResponse , JsonResponse

def homePage(request):
#     friends = [
#         'ankit',
#         'ram',
#         'shyam'
# ]
    employees=[  
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  
    {"name":"Bob", "email":"bob32@gmail.com"},  
    {"name":"Jai", "email":"jai87@gmail.com"}  
] 
    return JsonResponse(employees,safe=False)