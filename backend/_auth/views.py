# 📁 webappexample/views.py
import jwt
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, logout as django_logout
from urllib.parse import quote_plus, urlencode
from django.contrib.auth.decorators import login_required

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

# @login_required
def index(request):
    return render(
        request,
        "home.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )

def login(request):
    # Include 'next' parameter in the redirect URL
    redirect_uri = request.build_absolute_uri(reverse("callback"))
    redirect_uri += f"?next={request.GET.get('next', '/')}"
    
    return oauth.auth0.authorize_redirect(request, redirect_uri)


def callback(request):
    try:
        # Obtain access token and user information from OAuth
        token = oauth.auth0.authorize_access_token(request)
        request.session["user"] = token

        # Decode the ID token using pyjwt
        id_token_raw = token.get("id_token")
        id_token_decoded = jwt.decode(id_token_raw, options={"verify_signature": False})

        # Extract user information
        user_info = {
            "given_name": id_token_decoded.get("given_name"),
            "family_name": id_token_decoded.get("family_name"),
            "nickname": id_token_decoded.get("nickname"),
            "name": id_token_decoded.get("name"),
            "picture": id_token_decoded.get("picture"),
            "locale": id_token_decoded.get("locale"),
            "updated_at": id_token_decoded.get("updated_at"),
            "email": id_token_decoded.get("email"),
            "email_verified": id_token_decoded.get("email_verified"),
        }

        # Check if the 'email' key is present in user_info
        email = user_info.get('email')
        if email:
            # Check if a corresponding Django user exists
            user, created = User.objects.get_or_create(username=email, email=email)

            # Log in the Django user
            django_login(request, user)

            # Redirect to the original URL if 'next' is present in the query parameters
            next_url = request.GET.get('next', request.POST.get('next', '/'))
            return redirect(next_url if next_url != '/' else 'index')
        else:
            # Handle the case where 'email' is not present in user_info
            return redirect(reverse("login"))
    except Exception as e:
        # Handle exceptions by redirecting to login
        return redirect(reverse("login"))

def logout(request):
    django_logout(request)
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
