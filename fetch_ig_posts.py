import instaloader
import os

L = instaloader.Instaloader(
    download_pictures=True,
    download_videos=False,
    download_video_thumbnails=True,
    download_geotags=False,
    download_comments=False,
    save_metadata=True,
    compress_json=False
)

target_dir = os.path.join(os.path.dirname(__file__), "static", "ig_downloads")
os.makedirs(target_dir, exist_ok=True)

try:
    print("Fetching profile vanshikacooks...")
    profile = instaloader.Profile.from_username(L.context, "vanshikacooks")
    print(f"Profile: {profile.username}, Full name: {profile.full_name}, Posts: {profile.mediacount}")
    print(f"Biography: {profile.biography}")

    count = 0
    for post in profile.get_posts():
        print(f"Post {post.shortcode}: {post.caption[:80] if post.caption else 'No caption'}")
        L.download_post(post, target=target_dir)
        count += 1
        if count >= 15:
            break
    print(f"Successfully downloaded {count} posts!")
except Exception as e:
    print(f"Error fetching from instaloader: {e}")
