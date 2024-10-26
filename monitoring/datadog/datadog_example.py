from ddtrace import tracer

@tracer.wrap(name="custom_request_trace")
def process_request():
    time.sleep(random.random())
