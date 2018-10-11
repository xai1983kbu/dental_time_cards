from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime, date, time
from django.utils import timezone

# Create your views here.

from .forms import DateTimeForm, DeleteForm, DateEditForm
from .models import DaysAtWork


def current_month(request):
	form1 = DateTimeForm()
	form2 = DateEditForm()
	today_is = date.today()
	workday_list = DaysAtWork.objects.all().filter(date_work__year = today_is.year).filter(date_work__month = today_is.month)
	context = {
                'form1' : form1, 'form2': form2,
                'workday_list' : workday_list,
                # 'sum_per_month':sum_per_month,
                # 'salary_per_month':salary_per_month,
                # 'saturday':saturday,
                # 'today_is':today_is,
                # 'link_year':today_is.year, 'link_month':today_is.month,
                # 'date_error':date_error,
                }

	if request.method == 'POST':
		if 'add' in request.POST:
			form1 = DateTimeForm(request.POST)
			if form1.is_valid():
				date_in = request.POST.get('date_time_input_1')
				start_in = request.POST.get('date_time_input_2')
				end_in = request.POST.get('date_time_input_3')
				date_in = datetime.strptime(date_in, '%d/%m/%Y')
				try:
					#look up for the same date/dates
					date_match = DaysAtWork.objects.all().filter(date_work=date_in)
					#if exist then delete old dates
					date_match.delete()
					#saving new date data
					create_day = DaysAtWork(start_work=start_in, end_work=end_in, date_work=date_in, owner=request.user)
					create_day.save()
				except (KeyError, DaysAtWork.DoesNotExist):
				    #if does not exist just saving date data
				    create_day = DaysAtWork(start_work=start_in, end_work=end_in, date_work=date_in)
				    create_day.save()
				if today_is.month == date_in.month:
					return HttpResponseRedirect(reverse('salary:current_month'))
				else:
					return HttpResponseRedirect(reverse('salary:another_month', args=(date_in.year, date_in.month)))
		elif 'edit' in request.POST:
			form2 = DateEditForm(request.POST)
			if form2.is_valid():
				only_month_in = request.POST.get('date_time_input_4')
				only_month_in = datetime.strptime(only_month_in, '%Y/%m')
				return HttpResponseRedirect(reverse('salary:edit', args=(only_month_in.year, only_month_in.month)))
	return render(request, 'salary/current_month.html', context)


def another_month(request, year, month):
	form1 = DateTimeForm()
	form2 = DateEditForm()
	today_is = date.today()
	workday_list = DaysAtWork.objects.all().filter(date_work__year = year).filter(date_work__month = month)
	context = {
                'form1' : form1, 'form2': form2,
                'workday_list' : workday_list,
                }

	if request.method == 'POST':
		if 'add' in request.POST:
			form1 = DateTimeForm(request.POST)
			if form1.is_valid():
				date_in = request.POST.get('date_time_input_1')
				start_in = request.POST.get('date_time_input_2')
				end_in = request.POST.get('date_time_input_3')
				date_in = datetime.strptime(date_in, '%d/%m/%Y')
				try:
					#look up for the same date/dates
					date_match = DaysAtWork.objects.all().filter(date_work=date_in)
					#if exist then delete old dates
					date_match.delete()
					#saving new date data
					create_day = DaysAtWork(start_work=start_in, end_work=end_in, date_work=date_in)
					create_day.save()
				except (KeyError, DaysAtWork.DoesNotExist):
				    #if does not exist just saving date data
				    create_day = DaysAtWork(start_work=start_in, end_work=end_in, date_work=date_in)
				    create_day.save()
				if today_is.month == date_in.month:
					return HttpResponseRedirect(reverse('salary:current_month'))
				else:
					return HttpResponseRedirect(reverse('salary:another_month', args=(date_in.year, date_in.month)))
		elif 'edit' in request.POST:
			form2 = DateEditForm(request.POST)
			if form2.is_valid():
				only_month_in = request.POST.get('date_time_input_4')
				only_month_in = datetime.strptime(only_month_in, '%Y/%m')
				return HttpResponseRedirect(reverse('salary:edit', args=(only_month_in.year, only_month_in.month)))	
	return render(request, 'salary/another_month.html', context)


def edit(request, year, month):
	form1 = DeleteForm()
	form2 = DateEditForm()
	today_is = date.today()
	workday_list = DaysAtWork.objects.all().filter(date_work__year = year).filter(date_work__month = month)
	context = {
                'form1' : form1, 'form2' : form2,
                'workday_list' : workday_list,
                }

	if request.method == 'POST':
		if 'del' in request.POST:
			form1 = DeleteForm(request.POST)
			if form1.is_valid():
				choices_list = form1.cleaned_data.get('choices')
				for item in choices_list:
					item.delete()
		elif 'edit' in request.POST:
			form2 = DateEditForm(request.POST)
			if form2.is_valid():
				only_month_in = request.POST.get('date_time_input_4')
				only_month_in = datetime.strptime(only_month_in, '%Y/%m')
				return HttpResponseRedirect(reverse('salary:edit', args=(only_month_in.year, only_month_in.month)))
	return render(request, 'salary/edit.html', context)


# for key, value in request.POST.items():
	# print(key, value)
