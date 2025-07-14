def get_voice_message(status, complaint_flag=False, issue_type=None):
    if complaint_flag:
        return "Humein afsos hai, aapki complaint humare pass record ho gayi hai. Hum jald action lenge."
    
    if status == "arrived":
        return "Assalamu Alaikum! Aapki ride aa chuki hai. Shukriya WeRide use karne ka."
    elif status == "cancelled":
        return "Aapki ride cancel kar di gayi hai. Maafi chahtay hain."
    elif status == "in_progress":
        return "Aapki ride raste mein hai. Barah-e-karam thoda intezaar karein."
    else:
        return "Ride ki maloomat hasil nahi ho saki. Bara-e-karam dobara koshish karein."
