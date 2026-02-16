from flask import Flask, make_response, render_template, request, redirect, url_for



app = Flask(__name__)

# app = Flask(__name__, static_folder="assets")

#Enabling caching for static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600

#OR
#now modifying it for static files only
@app.after_request
def add_cache_control(response):

    # Disable cache for dynamic routes
    if request.endpoint != 'static':
        response.headers["Cache-Control"] = "no-store"

    return response



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/form")
# def form():
#     return render_template("form.html")


@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        name = request.form.get("name")
        age = request.form.get("age")

        error = None

        # Validation 1: Empty name
        if not name:
            error = "Name is required"

        # Validation 2: Empty age
        elif not age:
            error = "Age is required"

        # Validation 3: Age must be integer
        elif not age.isdigit():
            error = "Age must be a number"

        # Validation 4: Age condition
        elif int(age) < 18:
            error = "Age must be 18 or above"

        # If error exists → show form again
        # if error:
        #     return render_template("form.html", error=error)

        if error:
            return render_template("form.html", error=error, name=name, age=age)



        # If everything is correct
        return redirect(url_for("success", name=name, age=age))

    # GET request
    return render_template("form.html")


@app.route("/success")
def success():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("result.html", name=name, age=age)

# @app.route("/hotel")
# def hotel():
#     hotel_list = [
#         {"name": "Hotel A", "location": "City X", "rating": 4.5, "price": 10000},
#         {"name": "Hotel B", "location": "City Y", "rating": 4.0, "price": 150},
#         {"name": "Hotel C", "location": "City Z", "rating": 3.5, "price": 200},
#     ]
#     return render_template("hotel.html", hotels=hotel_list, admin=True)

@app.route("/hotel")
def hotel():

    hotel_list = [
        {"name": "Hotel A", "location": "City X", "rating": 4.5, "price": 10000},
        {"name": "Hotel B", "location": "City Y", "rating": 4.0, "price": 150},
        {"name": "Hotel C", "location": "City Z", "rating": 3.5, "price": 200},
    ]

    response = make_response(
        render_template("hotel.html", hotels=hotel_list, admin=True)
    )

    response.headers["Cache-Control"] = "public, max-age=300"
    return response




# @app.route("/submit",methods=["POST"])
# def submit():
#     name = request.form.get("name")
#     age = request.form.get("age")

#     return render_template("result.html", name = name, age = age)



# @app.route("/return/")
# def return_example():
#     name = request.args.get("name")
#     return render_template("result.html", name=name)

@app.route("/return", methods=["GET", "POST"])
def return_example():
    if request.method == "POST":
        # Get data from the form's 'name' attribute
        name = request.form.get("user_name")
        return f"Hello, {name}! This is a return example from a form."
    
    # If it's a GET request, just show the input page
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)


