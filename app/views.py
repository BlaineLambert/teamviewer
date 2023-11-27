from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    job: str
    members: list


teams = {
    "procurement": Team(
        name="Procurement",
        job="This team takes care of getting snacks, lunch, drinks, and managing a budget of $5 a day, 5 days a week, for each student.",
        members="Blaine, Adrian, Big John, Wyatt, Bryce",
    ),
    "documention": Team(
        name="Documention",
        job="This team details everything BCCA does thoughout the year including social media.",
        members="Conner, Kaleigh, Blair, Mina, Jay, Joshua, Kayleah",
    ),
    "community": Team(
        name="Community",
        job="This team takes care of events that we have every other week.",
        members="Jordan, Joby, Aj, Micah, Caleb",
    ),
    "management": Team(
        name="Management",
        job="This team makes sure we have the necessary supplies that we need and tells procurement what we need to buy.",
        members="Owen, Jeremiah, Nick, Ab, Abigail, Mathew",
    ),
}

# Create your views here.


def index(request: HttpRequest) -> render:
    context = {
        "leadershipteams": ["Procurement", "Community", "Documention", "Management"],
    }
    return render(request, "index.html", context)


def team(request: HttpRequest, team_name: str) -> HttpResponse:
    if team_name == "Management":
        return render(request, "team.html", {"result": teams["management"]})
    elif team_name == "Procurement":
        return render(request, "team.html", {"result": teams["procurement"]})
    elif team_name == "Documention":
        return render(request, "team.html", {"result": teams["documention"]})
    elif team_name == "Community":
        return render(request, "team.html", {"result": teams["community"]})
