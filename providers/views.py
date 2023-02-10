from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from providers.models import Provider
from providers.forms import ProviderForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def provider_list(request):
    providers = Provider.objects.filter(is_active = True)
    context = {
        'providers': providers
    }
    return render(request, 'providers/providers_list.html', context=context)

class ProviderListView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'providers/providers_list.html'

def create_provider(request):
    if request.method == 'GET':
        context = {
            'form': ProviderForm()
        }
        return render(request, 'providers/create_provider.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
          Provider.objects.create(
            name = form.cleaned_data['name'],
            address = form.cleaned_data['address'],
            email = form.cleaned_data['email'],
          )
          context = {
            'message': 'Provider created successfully'
          }           
        else:
            #Aca tenemos que manejar el error#
            context = {
                'form_errors': form.errors,
                'form': ProviderForm()
            }
        return render(request, 'providers/create_provider.html', context=context)

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/create_provider.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'

def provider_update(request, pk):
    provider = Provider.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form': ProviderForm(
                initial={
                    'name':provider.name,
                    'address': provider.address,
                    'phone_number': provider.phone_number,
                    'email': provider.email,
                }
            )
        }
        return render(request, 'providers/update_provider.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider.name = form.cleaned_data['name']
            provider.address = form.cleaned_data['address']
            provider.phone_number = form.cleaned_data['phone_number']
            provider.email = form.cleaned_data['email']
            provider.save()
          
            context = {
            'message': 'Provider updated successfully'
          }           
        else:
            context = {
                'form_errors': form.errors,
                'form': ProviderForm()
            }
        return render(request, 'providers/update_provider.html', context=context)

class ProviderUpdateView(UpdateView):
     model= Provider
     template_name = 'providers/update_provider.html'
     success_url = '/providers/providers-list/'
     fields = '__all__'

class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'providers/delete_provider.html'
    success_url = '/providers/providers-list/'




     