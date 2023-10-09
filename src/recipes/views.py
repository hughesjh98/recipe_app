from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .utils import get_recipename_from_id, get_chart
from .models import Recipe
import pandas as pd


# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin,ListView):
    model = Recipe
    
    template_name = 'recipes/recipes_main.html'
    
class RecipesDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    
    template_name = 'recipes/recipes_details.html'
    
@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    sales_df = None
    chart = None
    
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')    
        chart_type = request.POST.get('chart_type')    
        print(recipe_name, chart_type)
        
        qs = Recipe.objects.all()
        if qs:
            sales_df = pd.DataFrame(qs.values())
            
            # sales_df['id'] = sales_df['id'].apply(get_recipename_from_id)
            
            chart = get_chart(chart_type, sales_df, labels=sales_df['cooking_time'].values)
             
            sales_df = sales_df.to_html()
            

    context = {
        'form' : form,
        'sales_df' : sales_df,
        'chart' : chart
    }
            
    return render(request, 'recipes/records.html', context)