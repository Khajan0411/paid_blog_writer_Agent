def post_blog(blog_text, site_info):
    url = site_info['url']
    blog_id = site_info['blog_id']
    password = site_info['blog_password']

    # Simulate posting
    print(f"Posting to {url} as {blog_id}...")
    print(blog_text)
    return True

if __name__ == "__main__":
    post_blog("Sample blog content", {
        "url": "https://myblog.com",
        "blog_id": "admin",
        "blog_password": "123"
    })
