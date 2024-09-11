import requests

# Ganti dengan informasi Anda
username = "QiubyZ"
repo = "apk-autorelease"
token = "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"

headers = {"Authorization": f"token {token}"}

# Hapus semua rilis
releases_url = f"https://api.github.com/repos/{username}/{repo}/releases"
releases = requests.get(releases_url, headers=headers).json()
for release in releases:
    release_id = release["id"]
    delete_url = f"https://api.github.com/repos/{username}/{repo}/releases/{release_id}"
    requests.delete(delete_url, headers=headers)

# Hapus semua tag
tags_url = f"https://api.github.com/repos/{username}/{repo}/tags"
tags = requests.get(tags_url, headers=headers).json()
for tag in tags:
    tag_name = tag["name"]
    delete_url = f"https://api.github.com/repos/{username}/{repo}/git/refs/tags/{tag_name}"
    requests.delete(delete_url, headers=headers)

print("Semua rilis dan tag telah dihapus.")
