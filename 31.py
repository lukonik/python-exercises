def log_event(message: str, *args, **kwargs):
    print(
        f"message is: {message},args: {[str(arg) for arg in args]},kwargs: {[str(kwarg) for kwarg in kwargs.items()]}"
    )

log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
