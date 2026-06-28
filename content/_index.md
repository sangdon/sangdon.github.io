---
title: 'Sangdon Park'
date: 2023-10-24
type: landing
sections:
  - block: resume-biography
    content:
      # The user's folder name in content/authors/
      username: Sangdon Park
    design:
      spacing:
        padding: [0, 1rem, 0, 1rem] # top, right, bottom, left
      biography:
        style: 'text-align: left; font-size: 0.8em;'
  - block: collection
    content:
      title: 📄 Selected Publications
      filters:
        folders:
          - publication
        selected_only: true
      archive:
        enable: true
        link: /publication/
        text: See all
    design:
      view: pub-card
      spacing:
        padding: ['3rem', 0, '0rem', 0]
  - block: collection
    content:
      title: 📣 Recent News
      filters: 
        folders:
          - news
      archive:
        enable: true
        link: /news/
        text: See all
    design:
      spacing:
        padding: ['3rem', 0, '0rem', 0] # top, right, bottom, left
  - block: lab-photos
    content:
      title: 📸 Lab Photos
    design:
      spacing:
        padding: ['3rem', 0, '3rem', 0]
---


<!--- block: features-->
<!--  content:-->
<!--    title: Research Themes-->
<!--  items:-->
<!--    - name: Trustworthy Agentic AI-->
<!--      description: Safety, alignment, evaluation-->
<!--      icon: shield-check-->
<!--    - name: Large Code Models-->
<!--      description: Correctness + verification-->
<!--      icon: code-->
<!--    - name: RAG Reliability-->
<!--      description: Grounded generation + attribution-->
<!--      icon: database-->
<!--    - name: AI Security-->
<!--      description: Red teaming + robust systems-->
<!--      icon: lock-->
