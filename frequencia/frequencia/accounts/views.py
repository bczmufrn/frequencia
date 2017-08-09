from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse
from django.contrib.auth.models import Group
from django.forms import formset_factory, inlineformset_factory

from frequencia.vinculos.forms import AdicionarVinculoForm
from frequencia.vinculos.models import Vinculo

from .models import User
from .forms import RegisterForm, EditAccountForm


class AccountListView(ListView):
	paginate_by = 10
	model = User
	template_name = 'accounts/accounts.html'


def accounts_create(request):
	template_name = 'accounts/accounts_create_edit.html'

	VinculosFormset = formset_factory(AdicionarVinculoForm)
	
	form = RegisterForm(request.POST or None)

	vinculos_form = VinculosFormset(request.POST or None, prefix='vinculos')	

	if form.is_valid() and vinculos_form.is_valid():
		user = form.save()
		for vinculo_form in vinculos_form:			
			vinculo_form.save(user)
		return redirect('accounts:accounts')
	
	context = {
		'form': form,
		'vinculos_formset': vinculos_form,
	}
	return render(request, template_name, context)


def accounts_edit(request, pk): 
	template_name = 'accounts/accounts_create_edit.html'

	instance = get_object_or_404(User, pk=pk)
	form = EditAccountForm(request.POST or None, instance=instance)

	VinculosFormset = inlineformset_factory(User, Vinculo, exclude=('user',), extra=1, can_delete=False)
	vinculos_formset = VinculosFormset(request.POST or None, instance=instance, prefix='vinculos')

	if form.is_valid() and vinculos_formset.is_valid():
		form.save()
		vinculos_formset.save()
		return redirect('accounts:accounts')
	context = {
		'form': form,
		'vinculos_formset': vinculos_formset,
	}
	return render(request, template_name, context)


class Login(LoginView):
	template_name = 'accounts/login.html'
	
	def get_context_data(self, **kwargs):
		context = super(Login, self).get_context_data(**kwargs)
		context['landing_page'] = True
		return context


@login_required
def edit_password(request):
	template_name = 'accounts/edit_password.html'
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Senha alterada com sucesso!')
			context['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)
	context['form'] = form
	return render(request, template_name, context)

	

accounts = AccountListView.as_view()
# accounts_create = AccountCreateView.as_view()
#accounts_edit = AccountUpdateView.as_view()
login = Login.as_view()