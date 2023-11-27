from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass


@dataclass
class show:
    name: str
    desc: str
    cast: list


shows = {
    "friends": show(
        name="Friends",
        desc="Friends is a comedy series about six friends in their 20s and 30s who live in Manhattan, New York City. The show revolves around their personal and professional lives, their relationships, their struggles, and their joys1435. The show was created by Kevin S. Bright, Kauffman, and Crane, and starred Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry and David Schwimmer.",
        cast="Joseph Francis, Monica E. Geller, Phoebe Buffay-Hannigan, Chandler Bing, Ross Geller",
    ),
    "yellowstone": show(
        name="Yellowstone",
        desc="Yellowstone is an American neo-Western drama television series1that premiered on June 20, 2018, on Paramount Network. The series stars Kevin Costner, Luke Grimes, Kelly Reilly, Wes Bentley, Cole Hauser, Kelsey Asbille, and Gil Birmingham. The series follows the Dutton family, who controls the largest contiguous ranch in the United States, under constant attack by those it borders - land developers, an Indian reservation, and America's first National Park",
        cast="Kevin Costner, Luke Grimes, Kelly Reilly, Wes Bentley, Forrie J. Smith",
    ),
    "mandalorian": show(
        name="Mandalorian",
        desc="The Mandalorian is an American space Western television series created by Jon Favreau for the streaming service Disney+. It is the first live-action series produced in the Star Wars franchise, beginning five years after the events of Return of the Jedi (1983). The series stars Pedro Pascal as the title character, a lone bounty hunter who goes on the run to protect the Force-sensitive child Grogu from remnant Imperial forces led by Moff Gideon.",
        cast="Pedro Pascal, Katee Sackhoff, Carl Weathers, Werner Herzog",
    ),
    "simpsons": show(
        name="Simpsons",
        desc="The Simpsons is an American animated sitcom created by Matt Groening for the Fox Broadcasting Company. The series is a satirical depiction of American life, epitomized by the Simpson family, which consists of Homer, Marge, Bart, Lisa, and Maggie. Set in the fictional town of Springfield, it caricatures society, Western culture, television, and the human condition.",
        cast="Dan Castellaneta, Julie Kavner, Nancy Cartwright, Yeardley Smith, Hank Azaria, Harry Shearer",
    ),
}

# Create your views here.


def index(request: HttpRequest) -> render:
    context = {
        "shows_names": ["Simpsons", "Friends", "Yellowstone", "Mandalorian"],
    }
    return render(request, "index.html", context)


def display_shows(request: HttpRequest, show_name: str) -> HttpResponse:
    if show_name == "Simpsons":
        return render(request, "team.html", {"result": shows["simpsons"]})
    elif show_name == "Friends":
        return render(request, "team.html", {"result": shows["friends"]})
    elif show_name == "Yellowstone":
        return render(request, "team.html", {"result": shows["yellowstone"]})
    elif show_name == "Mandalorian":
        return render(request, "team.html", {"result": shows["mandalorian"]})
