---
layout: default
---

# Research Interests

My research interest focuses on designing <mark>trustworthy AI/ML systems</mark> by understanding from theory to
implementation and by considering practical applications in computer security, computer vision, natural language processing,
and cyber-physical systems, including robotics.

In particular, I'm currently interested in the following questions but very open to broader topics.

## Uncertainty Learning and Conformal Prediction

> <i class="fa-solid fa-circle-question"></i> **Can we rigorously learn and quantify the uncertainty of AI models, e.g., Large Language Models (LLMs), price predictors, or drones, under distribution shift and adversarial manipulation?**
> <br/>
> Quantified uncertainty of AI models' predictions provides a basis of the trust on predictions.
> To rigorously quantify uncertainty, 
> we have mainly leveraged learning theory and conformal prediction. 
> <br/>
> **Keywords**: `uncertainty quantification`, `learning theory`, `distribution shift`, `adversarial learning`, `conformal prediction`, `secure conformal prediction for security`, `LLMs` <br/>
> **Related Work**:
> [ICLR20](https://openreview.net/forum?id=BJxVI04YvB),
> [AISTATS20](http://proceedings.mlr.press/v108/park20b/park20b.pdf),
> [ICLR21](https://openreview.net/forum?id=Qk-Wq5AIjpq),
> [ICLR22](https://openreview.net/pdf?id=DhP9L8vIyLc),
> [arXiv22](https://arxiv.org/abs/2204.07482),
> [NeurIPS22](https://openreview.net/forum?id=s6ygs1UCOw1),
> [Security23](https://www.usenix.org/conference/usenixsecurity23/presentation/park),
> [arXiv23](https://arxiv.org/abs/2307.09254)

## Trustworthy LLMs

> <i class="fa-solid fa-circle-question"></i> **How to mitigate the <mark>hallucination problem</mark> of LLMs?**
> <br/>
> LMMs confidently generate wrong information, which undermines the trust of LLMs as a knowledge base.
> How to mitigate this?
> One way could be leveraging conformal prediction to measure uncertainty as a basis for trust
> (e.g., [[arXiv23](https://arxiv.org/abs/2307.09254)]).
> What other possibilities?
> <br/>
> **Keywords**: `uncertainty quantification`, `conformal prediction`, `LLMs` <br/>
> **Related Work**:
> [ICLR20](https://openreview.net/forum?id=BJxVI04YvB),
> [AISTATS20](http://proceedings.mlr.press/v108/park20b/park20b.pdf),
> [ICLR21](https://openreview.net/forum?id=Qk-Wq5AIjpq),
> [ICLR22](https://openreview.net/pdf?id=DhP9L8vIyLc),
> [arXiv22](https://arxiv.org/abs/2204.07482),
> [NeurIPS22](https://openreview.net/forum?id=s6ygs1UCOw1),
> [Security23](https://www.usenix.org/conference/usenixsecurity23/presentation/park),
> [arXiv23](https://arxiv.org/abs/2307.09254)

> <i class="fa-solid fa-circle-question"></i> **Can we discover and unlearn security and privacy issues in LLMs?**
> <br/>
> The power of LLMs and their daily life use bring concerns on security and privacy issues (e.g., vulnerable code generation and privacy leakage).
> Then, how severe are the security and privacy issues? How to unlearn the issues in LLMs?
> <br/>
> **keywords**: `LLMs`, `prompt tuning`, `machine unlearning` <br/>
> **Related Work**:
> [CVPR23](https://openaccess.thecvf.com/content/CVPR2023/papers/Si_Angelic_Patches_for_Improving_Third-Party_Object_Detector_Performance_CVPR_2023_paper.pdf)

## Trustworthy LLMs for Security

> <i class="fa-solid fa-circle-question"></i> **Can we leverage trustworthy LLMs to mitigate system security issues?**
> <br/>
> Finding source or binary code vulnerabilities is a long-standing and never-ending problem.
> The recent advance in LLMs potentially provides clues to further advance the current code vulnerability discovery performance.
> Can we leverage trustworthy LLMs for vulnerability discovery?
> <br/>
> **keywords**: `LLMs`, `vulnerability analysis` <br/>
> **Related Work**:
> [arXiv22](https://arxiv.org/abs/2211.00111)
