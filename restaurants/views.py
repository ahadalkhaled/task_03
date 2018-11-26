from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": 
    [
    	{
    	"restaurant_name": "Good Food",
    	"food_type": "Healthy",
    	},
    	{
    	"restaurant_name": "Bad Food",
    	"food_type": "Junk Food",
    	},
    	{
    	"restaurant_name": "All You Can Eat Food",
    	"food_type": "All types of cuisines.",
    	},
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    "my_object": {
            "restaurant_name":"Burger King",
            "food_type":"American Food",
            
        },

    }
    return render(request, 'detail.html', context)
