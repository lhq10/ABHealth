from django.shortcuts import render, redirect
from .models import Appointments, Providers, Services, ProviderServices
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def appointment(request):
    return render(request, 'appointment.html')

def about(request):
    providers = Providers.objects.all()  # Lấy tất cả provider từ database
    return render(request, 'about.html', {'providers': providers})

def create_appointment(request):
    if request.method == "POST":
        provider_id = request.POST.get('provider_id')
        appointment_date = request.POST.get('appointmentDate')
        selected_services = request.POST.getlist('services')  # Lấy danh sách dịch vụ được chọn

        provider = Providers.objects.get(pk=provider_id)

        # Tạo cuộc hẹn cho từng dịch vụ
        for service_id in selected_services:
            service = Services.objects.get(pk=service_id)
            Appointments.objects.create(
                CustomerID=request.user,  # Giả sử hệ thống đăng nhập đã có
                ProviderID=provider,
                ServiceID=service,
                AppointmentDate=appointment_date,
                Status='Pending',
            )

        messages.success(request, 'Lịch hẹn của bạn đã được tạo thành công!')
        return redirect('home')

    return redirect('home')

def get_provider_services(request, provider_id):
    provider_services = ProviderServices.objects.filter(ProviderID=provider_id)
    services = []
    for ps in provider_services:
        service = ps.ServiceID
        services.append({
            'ServiceID': service.ServiceID,
            'ServiceName': service.ServiceName,
            'Price': service.Price,
        })
    return JsonResponse({'services': services})

def test(request):
    return render(request, 'test.html')