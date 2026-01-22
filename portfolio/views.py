from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        if request.POST.get("company"):
            return redirect("/#contact")

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            EmailMessage(
                subject=f"ASDigital — New inquiry from {name}",
                body=(
                    f"Name: {name}\n"
                    f"Email: {email}\n\n"
                    f"Message:\n{message}\n"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECIPIENT_EMAIL],
                reply_to=[email],
            ).send(fail_silently=False)

            EmailMessage(
                subject="ASDigital Studio — we received your message",
                body=(
                    f"Hi {name}!\n\n"
                    "Thanks for reaching out to ASDigital Studio. We received your message and will reply soon.\n\n"
                    "Your message:\n"
                    f"{message}\n\n"
                    "— ASDigital Studio"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
                reply_to=[settings.EMAIL_HOST_USER],
            ).send(fail_silently=False)

            return redirect("/?sent=1#contact")

        return redirect("/?sent=0#contact")

    form = ContactForm()
    sent = request.GET.get("sent") == "1"
    return render(request, "portfolio/index.html", {"form": form, "sent": sent})