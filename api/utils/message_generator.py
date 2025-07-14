def generate_urdu_message(status):
    if status == "arrived":
        return "السلام علیکم! آپ کی رائڈ پہنچ چکی ہے۔ شکریہ WeRide استعمال کرنے کا۔"
    elif status == "cancelled":
        return "معذرت کے ساتھ! آپ کی رائڈ منسوخ کر دی گئی ہے۔"
    elif status == "delayed":
        return "ڈرائیور کچھ دیر میں پہنچے گا۔ براہ کرم پانچ منٹ انتظار کریں۔"
    elif status == "assigned":
        return "آپ کی رائڈ مختص کر دی گئی ہے، ڈرائیور راستے میں ہے۔"
    else:
        return "WeRide میں خوش آمدید! آپ کی درخواست پر کام جاری ہے۔"
