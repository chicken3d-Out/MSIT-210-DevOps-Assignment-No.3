from django.shortcuts import render

# Demo data (no DB yet)
ANNOUNCEMENTS = [
    {"id": 1, "title": "First Announcement", "content": "This is the full content of the first announcement."},
    {"id": 2, "title": "Second Announcement", "content": "This is the full content of the second announcement with more details."},
]

def announcement_list(request):
    return render(request, "myapp/list.html", {"announcements": ANNOUNCEMENTS})

def announcement_detail(request, pk):
    announcement = next((a for a in ANNOUNCEMENTS if a["id"] == pk), None)
    return render(request, "myapp/detail.html", {"announcement": announcement})
