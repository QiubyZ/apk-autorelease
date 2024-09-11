#!/bin/bash

username="QiubyZ" # Ganti dengan username GitHub kamu
repository="apk-autorelease" # Ganti dengan nama repository kamu

gh api graphql -F username="$username" -F reponame="$repository" -f '
query($username: String!, $reponame: String!) {
  repository(owner: $username, name: $reponame) {
    refs(refPrefix: "refs/tags/", first: 100) {
      nodes {
        name
      }
    }
  }
}
' --jq '.data.repository.refs.nodes[].name' | while read -r tag; do
  gh tag delete --force "$tag"
  echo "Tag '$tag' berhasil dihapus."
done
