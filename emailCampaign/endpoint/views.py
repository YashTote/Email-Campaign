from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import IntegrityError
import concurrent.futures
import time

def start_email(record):
    subject = record.campaign.subject
    message = 'Hello!'  # Plain text message (optional)
    from_email = 'yashtote99999@gmail.com'
    to_email = record.subscriber.email
    
    # Render the HTML content from the template
    html_message = render_to_string('mail_template.html', {'subscriber':record.subscriber.first_name ,'subject': record.campaign.subject,'preview_text' : record.campaign.preview_text, 'aritcle_url': record.campaign.article_url,
         'content': record.campaign.html_content, 'published_date' : record.campaign.published_date})

    # Generate the plain text message from the HTML content
    plain_message = strip_tags(html_message)

    try:
     delivery_record = DeliveryRecord(email=to_email)
     delivery_record.save()
     print("Record saved successfully.")
    except IntegrityError as e:
     print("Error:", e)

    # Send the email using send_mail
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)



@csrf_exempt
def send_email(request):
    if 'category' in request.GET:
        category = request.GET['category']
        print(category)
        records = CategoryRelationship.objects.filter(category__name=category, subscriber__is_active = True)
        t1 = time.perf_counter()
        print(records)
        with concurrent.futures.ThreadPoolExecutor(3) as executor:
            executor.map(start_email, records)
        
        # Ensure all threads have completed before proceeding
        executor.shutdown()
        
        t2 = time.perf_counter()
        
        # Serialize the queryset data to JSON
        data = [{'name': person.subscriber.email, 'campaign_title': person.campaign.title} for person in records]
        
        return JsonResponse({'people': data, 'execution_time': t2 - t1})
    else:
        return JsonResponse({'error': 'category parameter is missing'})


@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
      
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({'message': 'User with this email already exists'}, status=400)

        subscriber = Subscriber(email = email, first_name = user_name)
        subscriber.save()

        return JsonResponse({'message': 'User added successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def edit_user_status(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        active_status = request.POST.get('new_status')
        
        try:
            user = Subscriber.objects.get(email=email)
        except Subscriber.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
        
        user.is_active = active_status
        user.save()

        return JsonResponse({'message' : 'Email updated successfully'})
    else :
        return JsonResponse({'message': 'Invalid request method'}, status=405)