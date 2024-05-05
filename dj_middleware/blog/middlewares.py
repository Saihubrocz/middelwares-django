from datetime import datetime
current_time = datetime.now()
milliseconds = current_time.strftime("%H:%M:%S.%f")
def my_middleware(get_response):
    print("initializarin process",milliseconds)
    def my_function(request):
        print("functionality before running view.py",milliseconds)
        response = get_response(request)
        print("After views.py funtionality",milliseconds)
        return response
    return my_function