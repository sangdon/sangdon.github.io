---
title: Sequential Covariate Shift Detection Using Classifier Two-Sample Tests

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Sooyong Jang
- Sangdon Park
- Insup Lee
- Osbert Bastani

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2022-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-07-06T11:27:16.738498Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*International Conference on Machine Learning*'
publication_short: ''

doi: ''

abstract: A standard assumption in supervised learning is that the training data and
  test data are from the same distribution. However, this assumption often fails to
  hold in practice, which can cause the learned model to perform poorly. We consider
  the problem of detecting covariate shift, where the covariate distribution shifts
  but the conditional distribution of labels given covariates remains the same. This
  problem can naturally be solved using a two-sample test—i.e., test whether the current
  test distribution of covariates equals the training distribution of covariates.
  Our algorithm builds on classifier tests, which train a discriminator to distinguish
  train and test covariates, and then use the accuracy of this discriminator as a
  test statistic. A key challenge is that classifier tests assume given a fixed set
  of test covariates. In practice, test covariates often arrive sequentially over
  time—e.g., a self-driving car observes a stream of images while driving. Furthermore,
  covariate shift can occur multiple times—i.e., shift and then shift back later or
  gradually shift over time. To address these challenges, our algorithm trains the
  discriminator online. Additionally, it evaluates test accuracy using each new covariate
  before taking a gradient step; this strategy avoids constructing a held-out test
  set, which can improve sample efficiency. We prove that this optimization preserves
  the correctness—i.e., our algorithm achieves a desired bound on the false positive
  rate. In our experiments, we show that our algorithm efficiently detects covariate
  shifts on multiple datasets—ImageNet, IWildCam, and Py150.

# Summary. An optional shortened abstract.
summary: ''

tags:
- ICML

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: URL
  url: https://proceedings.mlr.press/v162/jang22a.html
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
