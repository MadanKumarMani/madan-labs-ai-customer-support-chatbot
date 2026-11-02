from tools.extract_tool import extract_customer_details


text = """
Hi my name is Madan from Mumbai.
I need underwater treadmill.
My phone number is 9876543210
"""


print(
    extract_customer_details(text)
)