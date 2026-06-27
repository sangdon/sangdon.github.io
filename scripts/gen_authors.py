#!/usr/bin/env python3
"""Generate content/authors/*/_index.md from data/team.json."""

import json
import os
import shutil

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEAM_JSON = os.path.join(REPO_ROOT, "data", "team", "team.json")
TEAM_BODY_DIR = os.path.join(REPO_ROOT, "team-src", "body")
TEAM_AVATARS_DIR = os.path.join(REPO_ROOT, "team-src", "avatars")
AUTHORS_DIR = os.path.join(REPO_ROOT, "content", "authors")


def render_profile(p):
    lines = [f"  - icon: {p['icon']}", f"    url: {p['url']}"]
    if p.get("label"):
        lines.append(f"    label: {p['label']}")
    return "\n".join(lines)


def render_org(o):
    lines = [f"  - name: {o['name']}"]
    if o.get("url"):
        lines.append(f"    url: {o['url']}")
    return "\n".join(lines)


def infer_avatar(member):
    first = member["first_name"].lower()
    last = member.get("last_name", "").lower()
    stem = f"{first}.{last}" if last else first
    for ext in ("jpg", "jpeg", "png", "webp"):
        path = os.path.join(TEAM_AVATARS_DIR, f"{stem}.{ext}")
        if os.path.exists(path):
            return path
    return None


def infer_folder(member):
    first = member["first_name"]
    last = member.get("last_name", "")
    if member["id"] == 0:
        return f"{first} {last}".strip()
    parts = [str(member["id"]), first.lower()]
    if last:
        parts.append(last.lower())
    return ".".join(parts)


def generate(member):
    first = member["first_name"]
    last = member.get("last_name", "")
    title = f"{first} {last}".strip()
    is_pi = member["id"] == 0
    superuser = str(is_pi).lower()
    highlight = str(is_pi).lower()

    orgs = "\n".join(render_org(o) for o in member.get("organizations", []))
    profiles = "\n".join(render_profile(p) for p in member.get("profiles", []))
    groups = "\n".join(f"  - {g}" for g in member.get("user_groups", []))
    website = member.get("website", "")
    bio = member.get("bio", "None")

    extra = ""
    for k, v in member.get("extra_frontmatter", {}).items():
        extra += f'\n{k}: "{v}"'

    content = f"""---
id: {member['id']}

# Display name
title: {title}

# Name pronunciation (optional)
name_pronunciation: "{member.get('name_pronunciation', '')}"

# Full name (for SEO)
first_name: {first}
last_name: {last}

# Status emoji
status:
  icon:

# Username (this should match the folder name)
authors:
  - {"" if not is_pi else title}

# Is this the primary user of the site?
superuser: {superuser}

# Role/position/tagline
role: {member.get('role', '')}

# Organizations/Affiliations to show in About widget
organizations:
{orgs}

# Short bio (displayed in user profile at end of posts)
bio: {bio}

# Social Networking
profiles:
{profiles}

# Highlight the author in author lists? (true/false)
highlight_name: {highlight}

# Author's website URL
website: "{website}"

# Organizational groups that you belong to (for People widget)
user_groups:
{groups}

disable_links: true{extra}
---
"""
    return content


def generate_group(member):
    group_name = member["user_groups"][0]
    active = [p["name"] for p in member.get("profiles", []) if p.get("active", True)]
    profiles = "\n".join(f"    - {p}" for p in active)
    return f"""---
title: {group_name}
profiles:
{profiles}
---
"""


def main():
    with open(TEAM_JSON, encoding="utf-8") as f:
        members = json.load(f)

    managed_folders = set()

    for member in members:
        if member.get("type") == "group":
            group_name = member["user_groups"][0].lower()
            out_path = os.path.join(AUTHORS_DIR, f"{group_name}.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(generate_group(member))
            print(f"Generated: {out_path}")
            continue

        folder = infer_folder(member)
        managed_folders.add(folder)
        out_dir = os.path.join(AUTHORS_DIR, folder)
        os.makedirs(out_dir, exist_ok=True)

        out_path = os.path.join(out_dir, "_index.md")
        content = generate(member)
        body_path = os.path.join(TEAM_BODY_DIR, f"{folder}.md")
        if os.path.exists(body_path):
            with open(body_path, encoding="utf-8") as bf:
                content += "\n" + bf.read()
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        avatar = infer_avatar(member)
        if avatar:
            ext = os.path.splitext(avatar)[1]
            shutil.copy2(avatar, os.path.join(out_dir, f"avatar{ext}"))

        print(f"Generated: {out_path}")

    # Warn about folders not in team.json (manually created, not deleted)
    for name in os.listdir(AUTHORS_DIR):
        if name in ("_index.md",) or name.endswith(".md"):
            continue
        folder_path = os.path.join(AUTHORS_DIR, name)
        if os.path.isdir(folder_path) and name not in managed_folders:
            print(f"WARNING: unmanaged author folder (not in team.json): {name}")


if __name__ == "__main__":
    main()
