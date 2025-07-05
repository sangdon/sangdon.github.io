---
title: Team
#date: 2022-10-24

type: landing

widget: people

sections:
  - block: people
    
    content:
      title: 
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Leader
          - PhD
          - MS
          - Admin
          - Intern
          - Alumni
          
      view_simple:
          - Intern
          - Admin 
           
      sort_by: Params.id
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
      spacing:
        padding: ["0", "1rem", "0", "1rem"]
    
---
