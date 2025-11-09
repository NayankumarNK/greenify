from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from usereg.models import UserProfile
from datetime import date  
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    context = {
        'eco_level': 'Intermediate',
        'user_points': 2430,
        'waste_recycled': '72 kg',
        'distance_biked': '88 km',
        'solar_hours': '35 hrs',
        'sustain_score': '91%',
        'user': request.user,
    }
    return render(request, 'usereg/home.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if not all([username, email, password, confirm]):
            messages.error(request, "Please fill in all fields.")
            return redirect('register')

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please login.")
        return redirect('login')

    return render(request, 'usereg/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # or dashboard
        else:
            # Check if username exists to provide specific feedback
            from django.contrib.auth.models import User
            if not User.objects.filter(username=username).exists():
                messages.error(request, "User not found. Please register first.")
            else:
                messages.error(request, "Incorrect password. Please try again.")

            return redirect('login')

    return render(request, 'usereg/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')
@login_required(login_url='login')
def profile(request):
    user = request.user

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')

        elif 'change_password' in request.POST:
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if not user.check_password(old_password):
                messages.error(request, 'Old password is incorrect.')
            elif new_password != confirm_password:
                messages.error(request, 'New passwords do not match.')
            else:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully! Please login again.')
                return redirect('login')

    context = {
        'username': user.username,
        'email': user.email,
        'eco_level': 'Intermediate',
        'user_points': 2430,
        'waste_recycled': '72 kg',
        'distance_biked': '88 km',
        'solar_hours': '35 hrs',
        'sustain_score': '91%',
        'user': user,
    }
    return render(request, 'usereg/profile.html', context)


# Example data, can come from a database model later
ECO_TIPS = [
        {"title": "Reduce Plastic Use", "description": "Carry reusable bags and avoid single-use plastics."},
        {"title": "Save Water", "description": "Turn off taps while brushing teeth and fix leaks."},
        {"title": "Energy Efficiency", "description": "Switch to LED bulbs and turn off unused appliances."},
        {"title": "Plant Trees", "description": "Plant native trees in your community or garden."},
        {"title": "Recycle Waste", "description": "Separate waste into recyclable and non-recyclable."},
        {"title": "Eco Transportation", "description": "Walk, bike, or use public transport whenever possible."},
    ]

@login_required(login_url='login')
def eco_tips(request):
    context = {
        'eco_tips': ECO_TIPS
    }
    return render(request, 'usereg/eco_tips.html', context)



@login_required(login_url='login')
def waste_management(request):
    # You can add data here later if needed
    return render(request, 'usereg/waste_management.html')


@login_required(login_url='login')
def water_conservation(request):
    tips = [
        {"title": "Fix Leaks", "desc": "Repair dripping taps and leaking pipes immediately."},
        {"title": "Water-Saving Fixtures", "desc": "Install low-flow showerheads, taps, and toilets."},
        {"title": "Reuse & Recycle", "desc": "Collect rainwater and reuse greywater for gardens."},
        {"title": "Mindful Usage", "desc": "Turn off taps while brushing or washing dishes."},
    ]
    return render(request, 'usereg/water_conservation.html', {"tips": tips})

def energy_conservation(request):
    return render(request, 'usereg/energy_conservation.html')


def carbon_footprint(request):
    return render(request, 'usereg/carbon_footprint.html')

def eco_challenges(request):
    return render(request, 'usereg/eco_challenges.html')

def progress_tracker(request):
    return render(request, 'usereg/progress_tracker.html')

def leaderboard(request):
    # 20 manually defined users with points
    users = [
        {"name": "Alice", "points": 95},
        {"name": "Bob", "points": 88},
        {"name": "Charlie", "points": 82},
        {"name": "David", "points": 80},
        {"name": "Eve", "points": 77},
        {"name": "Frank", "points": 74},
        {"name": "Grace", "points": 70},
        {"name": "Hannah", "points": 68},
        {"name": "Ivan", "points": 65},
        {"name": "Judy", "points": 63},
        {"name": "Kevin", "points": 60},
        {"name": "Laura", "points": 58},
        {"name": "Mallory", "points": 55},
        {"name": "Niaj", "points": 52},
        {"name": "Olivia", "points": 50},
        {"name": "Peggy", "points": 48},
        {"name": "Quinn", "points": 45},
        {"name": "Rupert", "points": 42},
        {"name": "Sybil", "points": 40},
        {"name": "Trent", "points": 38},
    ]
    return render(request, 'usereg/leaderboard.html', {"users": users})


def rewards(request):
    # Everything inside this function must be indented
    rewards_list = [
        {"name": "Eco Mug", "points": 100},
        {"name": "Reusable Bag", "points": 150},
        {"name": "Plant a Tree Voucher", "points": 200},
        {"name": "Solar Charger", "points": 300},
        {"name": "Eco T-Shirt", "points": 250},
        {"name": "Water Bottle", "points": 120},
        {"name": "Compost Bin", "points": 350},
        {"name": "Seed Kit", "points": 80},
        {"name": "LED Bulb Pack", "points": 180},
        {"name": "Bamboo Toothbrush", "points": 90},
        {"name": "Solar Lamp", "points": 400},
        {"name": "Organic Fertilizer", "points": 220},
        {"name": "Recycled Notebook", "points": 130},
        {"name": "Eco Backpack", "points": 500},
        {"name": "Reusable Straw Set", "points": 70},
        {"name": "Mini Herb Garden", "points": 160},
        {"name": "Eco Phone Case", "points": 210},
        {"name": "Recycled Pen Set", "points": 60},
        {"name": "Solar Fan", "points": 350},
        {"name": "Organic Soap Set", "points": 140},
    ]
    return render(request, "usereg/rewards.html", {"rewards": rewards_list})


def community(request):
    return render(request, 'usereg/community.html')

def articles(request):
    # Default articles
    articles_list = [
        {
            'title': '5 Easy Ways to Reduce Plastic Waste',
            'author': 'Greenify Team',
            'date': date(2025, 11, 8),
            'summary': 'Learn simple tips to reduce plastic usage at home, including reusable bags, bottles, and avoiding single-use plastics.'
        },
        {
            'title': 'Composting at Home',
            'author': 'Eco Expert',
            'date': date(2025, 11, 7),
            'summary': 'Step-by-step guide to composting kitchen and garden waste to make rich natural fertilizer for your plants.'
        },
        {
            'title': 'Saving Water with Smart Habits',
            'author': 'Hydro Green',
            'date': date(2025, 11, 6),
            'summary': 'Discover practical ways to save water daily, including fixing leaks, efficient showering, and rainwater harvesting.'
        },
        {
            'title': 'How to Reduce Your Carbon Footprint',
            'author': 'Carbon Neutral',
            'date': date(2025, 11, 5),
            'summary': 'Simple lifestyle changes like diet choices, transportation, and energy usage to reduce your environmental impact.'
        },
        {
            'title': 'Benefits of Plant-Based Diets',
            'author': 'Healthy Earth',
            'date': date(2025, 11, 4),
            'summary': 'Explore how reducing meat consumption can save resources, decrease emissions, and improve your health.'
        },
        {
            'title': 'Upcycling Old Items',
            'author': 'Creative Green',
            'date': date(2025, 11, 3),
            'summary': 'Transform old clothes, furniture, and household items into useful new products and reduce waste.'
        },
        {
            'title': 'The Importance of Tree Plantation',
            'author': 'Forest Friends',
            'date': date(2025, 11, 2),
            'summary': 'Learn why planting trees is critical for the environment and how you can contribute to local initiatives.'
        },
        {
            'title': 'Energy Efficient Homes',
            'author': 'Eco Architect',
            'date': date(2025, 11, 1),
            'summary': 'Tips for making your home energy-efficient with better insulation, lighting, and renewable energy options.'
        },
        {
            'title': 'Reducing E-Waste Safely',
            'author': 'Tech Green',
            'date': date(2025, 10, 31),
            'summary': 'Proper disposal and recycling of electronic items to reduce hazardous waste and recover valuable materials.'
        },
        {
            'title': 'Community Clean-Up Drives',
            'author': 'Neighborhood Green',
            'date': date(2025, 10, 30),
            'summary': 'How to organize and participate in community clean-ups to improve local environment and awareness.'
        },
    ]

    return render(request, 'usereg/articles.html', {'articles_list': articles_list})


@csrf_exempt
def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can save these to the database if you want
        print(f"Feedback received: {name}, {email}, {message}")
    return render(request, 'usereg/feedback.html')

def about(request):
    return render(request, 'usereg/about.html')
