import os

# Environment variable ka naam daalein, seedhe value nahi
API_ID = int(os.environ.get("24674775", "0"))
API_HASH = os.environ.get("51f65ab234b1495b13342e9c940a4701")
BOT_TOKEN = os.environ.get("8485300945:AAHIrkChp9yG4L6lS7_OLGNtNgBi9AfEH7U")
MONGO_URI = os.environ.get("mongodb+srv://1xc2xa:n9a4es@cluster0.c4vkgdl.mongodb.net/?retryWrites=true&w=majority")

# Payment keys
RAZORPAY_KEY = os.environ.get("rzp_test_RBGi023eo1h34b")
RAZORPAY_SECRET = os.environ.get("fvkaY2GBdO4UVvFwh2Zo1bSY")

# Bot Settings
DEFAULT_MUSIC_QUALITY = "high"
MAX_PLAYLISTS_FREE = 3