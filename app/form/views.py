from django.shortcuts import render
from app.form.forms import Opciones_gente_consciencia1, Opciones_politica_consciencia1, Opciones_capacidades_consciencia1, Opciones_gente_formalizacion1, Opciones_politica_formalizacion1, Opciones_capacidades_formalizacion1, Formprincipal
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response


""" def redirect_view(request):
    response = redirect('/form1/form2')
    return response """

def datos(request): 
    if request.method == 'POST': 
     form = Formprincipal(request.POST) 
     if form.is_valid(): 
        form.save()
        response = redirect('/form/form1')
        return response
    else: 
     form = Formprincipal
     return render(request,'formlario.html', {'form':form })

    

def countries_view(request): 
    if request.method == 'POST':
        form = Opciones_gente_consciencia1(request.POST)
        if form.is_valid():
            Opciones_gente_consciencia = form.cleaned_data.get('Opciones_gente_consciencia')
            if form.cleaned_data['pregunta_gente_conocmiento'] == '1':
                print(1)
            if form.cleaned_data['pregunta_gente_conocmiento'] == '2':
                print(2)
            if form.cleaned_data['pregunta_gente_conocmiento'] == '3':
                print(3)
            if form.cleaned_data['pregunta_gente_conocmiento'] == '4':
                print(4)
            if form.cleaned_data['pregunta_gente_conocmiento'] == '5':
                print(5)
            response = redirect('/form1/form2')
            return response
    else:
        form = Opciones_gente_consciencia1()
    return render(request, 'formulario1.html', {'form':form })


def countries_view1(request): 
    if request.method == 'POST': 
     form = Opciones_politica_consciencia1(request.POST) 
     if form.is_valid(): 
        Opciones_politica_consciencia= form.cleaned_data.get('Opciones_politica_consciencia') 
        if form.cleaned_data['Opciones_politica_consciencia'] == '1':
            print(1)
        if form.cleaned_data['Opciones_politica_consciencia'] == '2':
            print(2)
        if form.cleaned_data['Opciones_politica_consciencia'] == '3':
            print(3)
        if form.cleaned_data['Opciones_politica_consciencia'] == '4':
            print(4)
        if form.cleaned_data['Opciones_politica_consciencia'] == '5':
            print(5)
        response = redirect('/form2/form3')
        return response
    else: 
     form = Opciones_politica_consciencia1

    return render(request,'formulario2.html', {'form':form })

def countries_view2(request): 
    if request.method == 'POST': 
     form = Opciones_capacidades_consciencia1(request.POST) 
     if form.is_valid(): 
      countries = form.cleaned_data.get('countries') 
      response = redirect('/form3/form4')
      return response
    else: 
     form = Opciones_capacidades_consciencia1

    return render(request,'formulario3.html', {'form':form })

def countries_view3(request): 
    if request.method == 'POST': 
     form = Opciones_gente_formalizacion1(request.POST) 
     if form.is_valid(): 
      countries = form.cleaned_data.get('countries') 
      response = redirect('/form4/form5')
      return response
    else: 
     form = Opciones_gente_formalizacion1

    return render(request,'formulario4.html', {'form':form })
  
def countries_view4(request): 
    if request.method == 'POST': 
     form = Opciones_politica_formalizacion1(request.POST) 
     if form.is_valid(): 
      countries = form.cleaned_data.get('countries') 
     response = redirect('/form5/form5')
     return response
    else: 
     form = Opciones_politica_formalizacion1

    return render(request,'formulario5.html', {'form':form })

def countries_view5(request): 
    if request.method == 'POST': 
     form = Opciones_capacidades_formalizacion1(request.POST) 
     if form.is_valid(): 
      countries = form.cleaned_data.get('countries') 
      response = redirect('/form4/form5')
      return response
    else: 
     form = Opciones_capacidades_formalizacion1

    return render(request,'formulario6.html', {'form':form })

  
