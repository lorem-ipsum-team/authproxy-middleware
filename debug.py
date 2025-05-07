from config import DEBUG


def run_if_needed():
    if not DEBUG:
        return

    try:
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
    except Exception as e:
        print('Could not start debug server')
