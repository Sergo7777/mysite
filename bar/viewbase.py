def send_mail(request):
    if request.method == "POST":
            errors = {}
            if not errors:
                subject = ('Заказ стола в D.O.M')
                email = request.POST.get('email')
                table_id = request.POST.get('table_id').strip()
                if not table_id:
                    errors['table_id'] = 'Выберите стол'
                date = request.POST.get('date').strip()
                if not date:
                    errors['date'] = 'Введите дату'
                message = 'Вы заказали стол № {} на дату {}. Ждем Вас в нашем ресторане'.format(table_id, date)
                if subject and email and message:
                    try:
                        mail = EmailMessage(subject, message, 
                                        settings.EMAIL_HOST_USER, [email],)
                        mail.send()
                        Order.objects.create(date=request.POST['date'], 
                                name=request.POST['username'], email=request.POST['email'],
                                table_id=request.POST['table_id'])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('%s?status_message=Стол забронирован!' %
        reverse('table_list'))
            else:
                return render(request, 'bar/table_list.html', {'tables':tables, 'date_now': date_now, 'errors': errors})
