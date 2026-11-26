# Approach-now GPU buyers, 26 Nov 2026

**Target was 15 companies. Only 3 passed every rule.** I did not pad the list. The pool of new buyers that are not already in Raion's files is close to used up.

The rules were:
- the company is not already in the dedup or research files;
- it has a dated GPU-need signal from the last 60 days;
- it can pay;
- a new supplier is realistic;
- it is not a neocloud or chipmaker;
- it is not headquartered in a sanctioned country.

File: `approach-now-2026-11-26.csv`. It uses the daily-CSV columns plus `email`, `email_status` and `priority`.

## The 3 qualifiers

| # | Company | Fit | Why now | Decision makers with validated email |
|---|---|---|---|---|
| 1 | **Relace** (San Francisco) | 7 | Its homepage says "If you have GPUs, we'd also like to talk". It served 30T tokens in 30 days and volume grows about 3x a quarter. | Eitan Borgnia, Co-Founder & COO: eborgnia@relace.ai<br>Julian Thomassie, CTO: jthomassie@relace.ai |
| 2 | **Kape Technologies / ExpressVPN** (London) | 6 | ExpressAI already runs on Verda's confidential-computing B200 in the EU (22 Oct). The wider rollout is still pending. | Peter Membrey, CRO (quoted in the Verda story): peter.membrey@kape.com<br>Charles Butler, CEO: charles.butler@kape.com |
| 3 | **Epochal** (Palo Alto) | 5 | Launched 24 Nov with $100M of the CEO's own money to train forecasting models. No supplier is disclosed. | Not in Apollo. Use LinkedIn: Guodong Zhang, CEO; Zihang Dai and Manuel Kroiss, co-founders. |

**Email checks:** all 4 emails are Apollo "verified" and LeadMagic "validated" (26 Nov 2026). They are on catch-all domains, so a hard bounce is unlikely but still possible.

**Caveats**
- **Relace credit is weak.** It raised a $23M Series A in Oct 2025, and one block is about 30% of all the money it has raised. Offer a ramp, a prepay, or a smaller first tranche.
- **Kape is gated on confidential computing.** Raion must be able to offer multi-node confidential computing on Blackwell, which is what Verda gives them today.
- **Epochal was already in the 25 Nov notes** as a reject / watch lead. It now passes only on a literal reading: the $100M is the CEO's own money, not an outside round. Check whether the team already treats it as taken.

## Watch leads (not counted)
- **Cantina Labs** (Sean Parker; real-time video and voice AI).
  - On 20 Nov it posted a "Business Analyst, Infrastructure & Pricing Strategy" role, whose job is to "negotiate infrastructure agreements with compute and cloud providers, including spend commitments, capacity requirements": https://jobs.ashbyhq.com/cantina/d976abf0-5f73-4e37-9b21-c04468fa7795
  - Funding can't be confirmed (~$20–33M on aggregators, mixed up with other companies). It qualifies if a raise of $40M or more can be shown. **This is the best watch lead.**
- **Ellison Institute of Technology** (Oxford).
  - On 19 Nov it posted a Senior ML Infrastructure Engineer role to "forecast capacity and cost for GPU" needs.
  - It can pay, but Oracle reportedly supplies $5B of compute, so a new supplier is unlikely.
- Near misses from the other angles: LlamaIndex, Ludo Robotics (a Krafton subsidiary), Xlue and Holyvolt.

## Channel and sales notes
- **Sales positioning quote.** Transformer Lab's CEO on 9 Nov 2026: "Almost nobody has capacity available at any price… 3 years+… 25–50% up front."
- **Channel lead.** NVIDIA's $250M of UK AI-safety compute will be routed through UK NVIDIA Cloud Partners (TFN, 15 Oct 2026). This is relevant to the partner list in `../gpu-partners-2026-11/`.

## Angles searched (8)
1. Funding rounds of $30M+.
2. Inference-provider volume.
3. Neocloud customer stories.
4. Shortage statements.
5. EU and sovereign buyers.
6. Watch-list rechecks.
7. GPU and HPC hiring: about 700 names checked through job boards, LinkedIn, Workable and HN "Who is hiring".
8. Leftovers.

Almost every live signal belongs to a company already in Raion's files, an excluded company, a frontier lab, or a supplier.

**Suggested next angle:** funding-news and compute-statement monitoring, run daily. Hiring signals are used up.
