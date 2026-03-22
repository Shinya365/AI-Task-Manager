def predict_priority(task):
    task = task.lower()

    if "urgent" in task or "asap" in task:
        return "High"
    elif "later" in task:
        return "Low"
    else:
        return "Medium"
        