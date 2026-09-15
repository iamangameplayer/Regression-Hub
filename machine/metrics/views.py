from django.shortcuts import render

def metrics(request):
    return render(request, 'metrics_page.html')


def model_comparison(request):
    models = [

        {
            "name": "Linear Regression",
            "r2":0.62,
            "mae":0.50,
            "mse":0.51,
            "rmse":0.72,
        },

        {
            "name": "Ridge Regression",
            "r2":0.59,
            "mae":0.54,
            "mse":0.54,
            "rmse":0.74,
        },
        {
            "name": "Random Forest Regression",
            "r2":0.82,
            "mae":0.35,
            "mse":0.24,
            "rmse":0.49,
        },
        {
            "name": "Gradient Boosting Regression",
            "r2":0.84,
            "mae":0.33,
            "mse":0.21,
            "rmse":0.46,
        },
        {
            "name": "KNN Regression",
            "r2":0.76,
            "mae":0.40,
            "mse":0.32,
            "rmse":0.57,
        },
        {
            "name": "XGBoost Regression",
            "r2":0.87,
            "mae":0.30,
            "mse":0.17,
            "rmse":0.41,
        }
    ]

    return render(request,
"model_comparison.html", {"models":models,"best_model":"XGBoost Regression"})